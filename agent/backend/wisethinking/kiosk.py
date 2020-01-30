from string import ascii_lowercase, ascii_uppercase
from wisethinking.config import Config
from wisethinking.wfserial import WfSerial
import datetime
import time
import threading
import os
import re
import sys
import math

DEBUG = False


class KioskHandler():
    """키오스크를 다루는 상위클래스
    """
    CNT_TO_ASCII = ' ' + ascii_uppercase.replace('P', '')
    CASH_CODES = {
        '1': 1000,
        '2': 5000,
        '3': 10000,
        '4': 50000
    }
    PAYMENT_PROCESS_FILENAME = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'payment_process')
    STOP_FILENAME = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'stop')

    def __init__(self):
        """키오스크 클래스 생성자
        """
        _config = Config()
        self._config = _config.get_config('kiosk')
        self._coin_dev = self._config.get('coin_dev', 'COM3')
        self._cash_dev = self._config.get('cash_dev', 'COM4')
        self._card_dev = self._config.get('card_dev', 'COM6')

    def _save_payment_process(self, inserted, t):
        ret = True
        if os.path.exists(KioskHandler.STOP_FILENAME):
            os.unlink(KioskHandler.STOP_FILENAME)
            ret = False

        if os.path.exists(KioskHandler.PAYMENT_PROCESS_FILENAME):
            while True:
                try:
                    time.sleep(0.5)
                    os.unlink(KioskHandler.PAYMENT_PROCESS_FILENAME)
                    break
                except Exception as e:
                    print(e)

        print(inserted, t)
        with open(KioskHandler.PAYMENT_PROCESS_FILENAME, 'w') as f:
            f.write('{}\n{}'.format(inserted, t))

        return ret

    def cancel_payment_process(self):
        p = self.get_payment_process()

        if not self.is_payment_cleared():
            with open(KioskHandler.STOP_FILENAME, 'w') as f:
                f.write('aa')

            while not self.is_payment_cleared():
                time.sleep(0.2)

            if os.path.exists(KioskHandler.STOP_FILENAME):
                os.unlink(KioskHandler.STOP_FILENAME)

        return p

    def is_payment_cleared(self):
        return (not os.path.exists(KioskHandler.PAYMENT_PROCESS_FILENAME))

    def get_payment_process(self):
        if not os.path.exists(KioskHandler.PAYMENT_PROCESS_FILENAME):
            return {}

        with open(KioskHandler.PAYMENT_PROCESS_FILENAME, 'r') as f:
            res = {}
            res['money'] = f.readline().strip()
            res['t'] = f.readline().strip()

            return res
        return {}

    def clear_payment_process(self):
        if os.path.exists(KioskHandler.PAYMENT_PROCESS_FILENAME):
            while True:
                try:
                    time.sleep(0.5)
                    os.unlink(KioskHandler.PAYMENT_PROCESS_FILENAME)
                    break
                except Exception as e:
                    print(e)

    def wait_and_get_for_card(self, money, timeout=120):
        card_kiosk = KioskHandler.CardKioskHandler(self._card_dev, money)
        card_kiosk.start()

        t = datetime.datetime.now()
        t2 = datetime.datetime.now() - t
        while t2.seconds < timeout:
            time.sleep(0.25)
            t2 = datetime.datetime.now() - t
            if card_kiosk.stopped():
                break

            if not self._save_payment_process(card_kiosk.inserted_money, int(t2.seconds)):
                card_kiosk.stop()
                self.clear_payment_process()
                break

        if not card_kiosk.stopped():
            card_kiosk.stop()
            self.clear_payment_process()

        money = card_kiosk.join()
        return money

    def cancel_cash_dev(self):
        try:
            with WfSerial(self._cash_dev) as serial:
                serial.write('\x06\x20\x21B', crc=True)
        except:
            pass

    def wait_and_get_for_cash(self, timeout=120):
        try:
            cash_kiosk = KioskHandler.CashKioskHandler(self._cash_dev)
            cash_kiosk.start()
        except:
            return

        t = datetime.datetime.now()
        t2 = datetime.datetime.now() - t
        while t2.seconds < timeout:
            time.sleep(0.25)
            t2 = datetime.datetime.now() - t
            money = cash_kiosk.inserted_money

            if cash_kiosk.stopped():
                break

            if not self._save_payment_process(money, int(t2.seconds)):
                cash_kiosk.stop()
                self.clear_payment_process()
                break

        if not cash_kiosk.stopped():
            cash_kiosk.stop()
            self.clear_payment_process()

        money = cash_kiosk.join()

        return money

    def send_coins(self, cnt, target):
        """키오스크에 코인 수를 전달

        Paramenters
        -----------
        cnt: integer
            코인 수
        target: integer
            코인 수를 전달할 장비 정보
        device channel: str
            0x41~0x4F (1~15, A~O)
        pulse channel: str
            0x51~0x55 (1~5, Q~U)
        RESET: str
            0x56 (V)
        Status: integer
            0x80 (0x80)
        DATA1: str
            0x01~0x1E (SOH~RS)
        DATA2: integer
            None
        """
        # commands = chr(int(target) + 96) + KioskHandler.CNT_TO_ASCII[cnt]        
        # commands *= 3
        commands = '\x07\x41\x01\x00'
        try:
            with WfSerial(self._coin_dev) as serial:
                serial.write(commands, crlf=False, crc=True)
        except Exception as e:
            print(e)
            return False

        return True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return

    def send_reset(self, target):
        """키오스크에 코인 수를 전달

        Paramenters
        -----------
        target: string
            코인 수를 전달할 장비 정보
        """
        commands = '\x07\x56\x01\x00'
        # commands = chr(int(target) + 96) + 'U'
        # commands *= 3
        try:
            with WfSerial(self._coin_dev) as serial:
                serial.write(commands, crlf=True)
        except:
            return False

        return True

    def send_shutdown(self, target):
        """키오스크에 코인 수를 전달

        Paramenters
        -----------
        target: string
            코인 수를 전달할 장비 정보
        """

        commands = chr(int(target) + 96) + 'V'
        commands *= 3
        try:
            with WfSerial(self._coin_dev) as serial:
                serial.write(commands, crlf=True)
        except:
            return False

        return True

    def send_start(self, target):
        """키오스크에 코인 수를 전달

        Paramenters
        -----------
        target: string
            코인 수를 전달할 장비 정보
        """

        commands = chr(int(target) + 96) + 'V'
        commands *= 3
        try:
            with WfSerial(self._coin_dev) as serial:
                serial.write(commands, crlf=True)
        except:
            return False

        return True

    def send_upgrade(self, isupgrade):
        """키오스크에 업그레이드 신호 전달"""
        return isupgrade

    class CashKioskHandler(threading.Thread):
        def __init__(self, dev):
            super(KioskHandler.CashKioskHandler, self).__init__()
            self.wf = WfSerial(dev)
            self._stop_event = threading.Event()
            self.inserted_money = 0

        def stop(self):
            try:
                if self.wf.is_open():
                    self.wf.write('\x06\x20\x21B', crc=True)
                    time.sleep(2)
                self.wf.close()
                self._stop_event.set()
            except Exception as e:
                print(e)

        def stopped(self):
            return self._stop_event.is_set()

        def run(self):
            if DEBUG:
                self.inserted_money = 0
                while self.inserted_money < 6000:
                    time.sleep(2)
                    self.inserted_money += 1000
            else:
                try:
                    self.wf.write('\x06\x20\x21A', crc=True)
                    res = self.wf.read(5)
                    # Cannot open device
                    if res[3] != 0:
                        return False

                    self.inserted_money = 0
                    while True:
                        res = self.wf.read(5)

                        if res == b'\x06 !\x00\x07':
                            break

                        if res == b'':
                            break

                        if str(res[3]) not in KioskHandler.CASH_CODES:
                            continue

                        self.inserted_money += KioskHandler.CASH_CODES[str(
                            res[3])]
                        print(self.inserted_money)
                except Exception as e:
                    print(e)

            self.stop()

        def join(self):
            super(KioskHandler.CashKioskHandler, self).join()
            return self.inserted_money

    class CardKioskHandler(threading.Thread):
        def __init__(self, dev, money):
            super(KioskHandler.CardKioskHandler, self).__init__()
            self._money = money
            self.wf = WfSerial(dev, baudrate=115200)
            self._stop_event = threading.Event()
            self.inserted_money = 0

            _config = Config()
            self.cardkey = _config.get_config('agency').get('cardkey', '')
            if self.cardkey:
                self.cardkey = str(self.cardkey)
            
            now = datetime.datetime.now()
            t = now.strftime('%Y%m%d%H%M%S')
            data = '\x02'
            data += self.cardkey + ' ' * (16-len(self.cardkey))
            data += t
            data += 'B'
            data += '\x00'
            data += '\x1E\x00'
            data += '1'
            data += '0'*(10-len(str(self._money))) + str(self._money)
            real = self._money-(self._money*(1/1.1))
            data += '0'*(8-len(str(int(float(str(real)))))) + str(int(float(str(real))))
            # data += '00000000' # for test case
            data += '00000000'
            data += '00'
            data += '1'
            data += '\x03'
            
            self.approve_data = data
            now = datetime.datetime.now()
            t = now.strftime('%Y%m%d%H%M%S')
            data = '\x02'
            data += self.cardkey + ' ' * (16-len(self.cardkey))
            data += t
            data += 'E'
            data += '\x00'
            data += '\x1E\x00'
            data += '1'
            data += '0'*(10 - len(str(self._money))) + str(self._money)
            data += '00000000'
            data += '00000000'
            data += '00'
            data += '1'
            data += '\x03'
            self.cancel_data = data
            now = datetime.datetime.now()
            t = now.strftime('%Y%m%d%H%M%S')
            data = '\x02'
            data += self.cardkey + ' ' * (16-len(self.cardkey))
            data += t
            data += 'R'
            data += '\x00'
            data += '\x00\x00'
            data += '\x03'
            self.reset_data = data

        def stop(self):
            self._stop_event.set()
            if self.wf.is_open():
                try:
                    self.wf.write(self.cancel_data, crc=True)
                except:
                    pass
            try:
                self.wf.close()
            except:
                pass

        def stopped(self):
            return self._stop_event.is_set()

        def run(self):
            if not self.cardkey:
                self.stop()
                return False

            if DEBUG:
                time.sleep(5)
                self.inserted_money = self._money
            else:
                self.wf.write(self.approve_data, crc=True)
                res = self.wf.read()
                # Cannot open device
                if res != b'\x06':
                    return False

                buf = b''
                flag = False
                while True:
                    res = self.wf.read()

                    if res == b'\x02':
                        buf = b''

                    buf += res

                    if len(buf) >= 32:
                        if buf[31] == 101:  # fail => wait mode
                            break

                    if flag:
                        # and buf[35] == 79: # 79: 'O'
                        if len(buf) >= 37 and buf[31] == 64:
                            break

                    if len(buf) == (157+37) and buf[31] == 98:
                        if buf[35] == 49:  # success b'1'
                            self.inserted_money = self._money
                            flag = True

            self.stop()

        def join(self):
            super(KioskHandler.CardKioskHandler, self).join()
            return self.inserted_money


if __name__ == "__main__":
    with KioskHandler() as kiosk:
        kiosk.send_coins(10, 1)

    # with KioskHandler() as kiosk:
    #     res = kiosk.wait_and_get_for_card(2000, 10)
    #     print(res)
