import datetime
import requests
import os
import signal
import sys
import time
import threading
import logging
import shutil
from logging.handlers import RotatingFileHandler
from flask_cors import CORS, cross_origin
from selenium import webdriver
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
from threading import Timer
from wisethinking.config import Config
from wisethinking.kiosk import KioskHandler
from wisethinking.server import ServerHandler
from wisethinking.server_command import ServerCommands
from flask_socketio import SocketIO, emit

DEBUG = False

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, 'static'))
CORS(app)

socketio = SocketIO(app)

class ChromeMonitor(threading.Thread):
    def __init__(self):
        self._start_chrome()
        super(ChromeMonitor, self).__init__()
        self._stop_event = threading.Event()
        self._chrome_stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()
        while self.is_alive():
            print('Wait for closing chrome')
            time.sleep(1)

        self._close_chrome()

    def chrome_stop(self):
        self._chrome_stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        while not self.stopped():
            #print('monitoring...') #기존구문
            time.sleep(5)
            try:
                if self._chrome_stop_event.is_set():
                    self._chrome_stop_event.clear()
                    self._close_chrome()
                    self._start_chrome(3)
                elif not self._driver.window_handles:
                    self._close_chrome()
                    self._start_chrome(3)
                elif not self._driver:
                    self._close_chrome()
                    self._start_chrome(3)
            except Exception as e:
                print(e)
                # It is handled by stop function
                if 'chrome not reachable' in str(e):
                    self._start_chrome(3)

    def _start_chrome(self, refresh_time=2):
        binary = 'chromedriver.exe'
        # binary = 'chromedriver_v73.exe'
        if os.name == 'posix':
            binary = 'chromedriver.mac'

        google = os.path.join(BASE_DIR, 'Chrome')
        tmp_dir = os.getenv('TEMP')
        tmp_dirs = os.listdir(tmp_dir)
        for t in tmp_dirs:
            if t[:10] == 'scoped_dir':
                shutil.rmtree(os.path.join(tmp_dir, t), ignore_errors=True)

        opts = webdriver.ChromeOptions()
        opts.add_argument('--kiosk')
        opts.add_argument('--incognito')
        opts.add_argument('--disable-infobars')
        opts.add_argument('user-data-dir=' + google)
        self._driver = webdriver.Chrome(os.path.join(
            BASE_DIR, 'bin', binary), options=opts)

        # After 2 seconds, go to server
        # 'http://127.0.0.1:4000'
        Timer(refresh_time, lambda d: d.get('http://127.0.0.1:4000'), args=(self._driver,)).start()

    def _close_chrome(self):
        try:
            self._driver.close()
        except:
            pass

        try:
            self._driver.quit()
        except:
            pass


if not DEBUG:
    commands = ServerCommands()
    monitor = ChromeMonitor()


@socketio.on('cancel-payment')
def socket_cancel_payment(msg=None):
    time.sleep(0.3)

    app.logger.info('SOCKET /cancel-payment')
    with KioskHandler() as kiosk:
        p = kiosk.cancel_payment_process()


@app.route('/reboot', methods=['GET'])
def reboot():
    if os.name == 'nt':
        if not DEBUG:
            monitor.stop()
            commands.stop()
        import subprocess
        subprocess.call('shutdown /r /t 0'.split(' '))


@app.route('/cancel-payment', methods=['GET'])
def cancel_payment():
    res = {
    }
    with KioskHandler() as kiosk:
        p = kiosk.cancel_payment_process()
        if p:
            res['money'] = int(p)

    return jsonify(res), 200


@app.route("/cash/status", methods=['GET'])
def cash_status():
    with KioskHandler() as kiosk:
        res = kiosk.get_payment_process()

        return jsonify(res), 200

    return jsonify(res), 400


@app.route("/cash/call", methods=['POST'])
def cash_request():
    data = request.get_json()
    app.logger.info('POST /cash/call: ' + str(data))

    with KioskHandler() as kiosk:
        res = kiosk.wait_and_get_for_cash()
        kiosk.clear_payment_process()
        if res is None:
            app.logger.error('GET /cash/call 400: cannot open cash board')
            return jsonify({'money': 0}), 400

    app.logger.info('GET /cash/call 200')
    return jsonify({'money': res}), 200


@app.route("/card/status", methods=['GET'])
def card_status():
    with KioskHandler() as kiosk:
        res = kiosk.get_payment_process()

        return jsonify(res), 200

    return jsonify(res), 400


@app.route("/card/call", methods=['POST'])
def card_request():
    data = request.get_json()
    money = data.get('money', None)
    app.logger.info('POST /card/call: ' + str(data))

    if not money:
        app.logger.info('POST /card/call: no money 400')
        return jsonify('[]'), 400

    with KioskHandler() as kiosk:
        res = kiosk.wait_and_get_for_card(money)
        kiosk.clear_payment_process()

    app.logger.info('POST /card/call: 200')
    return jsonify({'money': res}), 200


@app.route("/build", methods=['GET'])
def build():
    _now = datetime.datetime.now()
    app.logger.info('GET /build')
    _server = ServerHandler()
    _config = Config()

    kid = _config.get_config('agency').get('kid', None)
    
    if not kid:
        return jsonify('[]'), 400

    results = {}
    res = _server.do_api('/agency-account/{}'.format(kid))
    if res.status_code != 200:
        return jsonify('[]'), 400
    results['agency'] = res.json().get('agency')

    exp = map(int, results['agency'].get('expire_date').split('-'))
    if datetime.date(*exp) < datetime.date.today():
        return jsonify({"err": "expired"}), 400

    res = _server.do_api('/point')
    if res.status_code != 200:
        app.logger.error('server /point: {}'.format(res.text))
        return jsonify('[]'), 400
    results['agency']['use_point'] = res.json().get('use_point')

    types = (
        'washer', 'dryer', 'tromm', 'shoes-washer', 'shoes-dryer',
        'airconditioner', 'supplies'
    )

    results['devices'] = {}
    devices_info = {}
    for idx, key in enumerate(types):
        res = _server.do_api('/agency-devices?type={}'.format(idx))
        if res.status_code != 200:
            app.logger.error(
                'server /agency-devices(type:{}): {}'.format(key, res.text))
            return jsonify('[]'), 400
        results['devices'][key] = res.json().get('results')

        if results['devices'][key]:
            for device_idx, _device in enumerate(results['devices'][key]):
                device_id = _device['id']
                if idx >= 2:
                    # etc devices
                    results['devices'][key][device_idx]['device'] = results['devices'][key][device_idx].pop(
                        'etcDevice')
                else:
                    del(results['devices'][key][device_idx]['etcDevice'])

                res = _server.do_api(
                    '/agency-courses?device_id={}'.format(device_id))
                if res.status_code != 200:
                    app.logger.error(
                        'server /agency-courses(device_id:{}): {}'.format(device_id, res.text))
                    return jsonify('[]'), 400
                results['devices'][key][device_idx]['courses'] = res.json().get(
                    'results')

                if key not in devices_info:
                    devices_info[key] = []

                devices_info[key].append(
                    results['devices'][key][device_idx]['controller_id'])

    _diff = datetime.datetime.now() - _now
    if _diff.seconds <= 15:
        _config.update_config('devices', devices_info)
    else:
        app.logger.error('Network is too slow')

    res = _server.do_api('/tubelink')
    if res.status_code != 200:
        results['youtube'] = 'https://www.youtube.com/embed/_XTNFR2ZTwQ'
    else:
        results['youtube'] = res.json().get('link_path')

    # if 'v=' in results['youtube']:
    #     results['youtube'] = results['youtube'].split('v=')[-1]
    # else:
    #     results['youtube'] = results['youtube'].split('/')[-1]

    return jsonify(results), 200


@app.route("/init", methods=['GET', 'POST'])
def init_check():
    if request.method == 'GET':
        app.logger.info('GET /init:')
        config = Config()
        agency = config.get_config('agency')
        
        if 'seckey' not in agency:
            return jsonify('[]'), 400

        return jsonify('[]'), 200
    else:
        data = request.get_json()
        app.logger.info('POST /init: ' + str(data))
        kid = data.get('kid', None)
        seckey = data.get('seckey', None)
        cardkey = data.get('cardkey', None)

        if not (kid and seckey):
            return jsonify('[]'), 400

        _server = ServerHandler()
        if not _server.is_correct_keys(kid, seckey):
            return jsonify('[]'), 400

        config = Config()
        agency = config.get_config('agency')
        agency['kid'] = kid
        agency['seckey'] = seckey
        if cardkey:
            agency['cardkey'] = cardkey

        config.update_config('agency', agency)

        return jsonify('[]'), 200

    return jsonify('[]'), 400


@app.route("/server", methods=['POST'])
def server():
    data = request.get_json()
    app.logger.info('POST /server: ' + str(data))

    method = data.get('method', None)
    path = data.get('path', None)
    args = data.get('args', None)

    if not (method and path):
        app.logger.error('POST /server: 400 no argument')
        return jsonify('[]'), 400

    _server = ServerHandler()

    try:
        res = _server.do_api(uri=path, data=args, reqtype=method.upper())
    except:
        app.logger.error('POST /server: 400 server failure')
        return jsonify('[]'), 400

    if res.status_code // 100 == 2:
        app.logger.info(res.text)
        return jsonify(res.json()), 200

    app.logger.info('POST /server: server failure ' + str(res.status_code))
    return jsonify('[]'), res.status_code


@app.route("/trigger", methods=['POST'])
def trigger():
    _unit = 500
    data = request.get_json()
    price = data.get('price', 0)
    target = data.get('target', 0)

    app.logger.info('POST /trigger: ' + str(data))

    # Validate
    if not target:
        app.logger.error('POST /trigger: 400 no target')
        return jsonify('[]'), 400

    if not price:
        app.logger.error('POST /trigger: 400 no price')
        return jsonify('[]'), 200

    try:
        price = int(price)
        target = int(target)
    except:
        app.logger.error('POST /trigger: 400 no int price and target')
        return jsonify('[]'), 400

    if price % _unit:
        app.logger.error('POST /trigger: 400 wrong price')
        return jsonify('[]'), 400

    coins = price // _unit
    print(coins, price, _unit)
    with KioskHandler() as kiosk:
        if not kiosk.send_coins(coins, target):
            app.logger.error('send coins failure {}, {}'.format(coins, target))
            return jsonify('[]'), 400

    app.logger.info('POST /trigger: 200')
    return jsonify('[]'), 200


@app.route("/shutdown", methods=['GET'])
def shutdown():
    monitor.chrome_stop()

    return jsonify('[]'), 200


@app.route("/", methods=['GET'])
def root():
    return render_template('index.html')


def main():
    if not DEBUG:
        commands.start()
        monitor.start()

        def _signal_hadnler(*args):
            print('Close Washfriends agent...')
            monitor.stop()
            commands.stop()
            sys.exit(0)

        signal.signal(signal.SIGINT, _signal_hadnler)

        formatter = logging.Formatter(
            "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
        handler = RotatingFileHandler(os.path.join(
            BASE_DIR, 'agent.log'), maxBytes=10000, backupCount=1024)
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)

        app.logger.addHandler(handler)
        app.logger.setLevel(logging.INFO)
        
    socketio.run(app, host='127.0.0.1', port=4000)


if __name__ == "__main__":
    main()
