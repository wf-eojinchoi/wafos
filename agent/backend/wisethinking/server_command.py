import threading
import time
import os
import json
import winsound
import requests
import zipfile
from wisethinking.server import ServerHandler
from wisethinking.kiosk import KioskHandler
from wisethinking.config import Config
from flask import Flask, redirect, url_for, render_template



class ServerCommands(threading.Thread):
    def __init__(self):
        super(ServerCommands, self).__init__()
        self._handler = ServerHandler()
        self._stop_event = threading.Event()
        self._isupgrade = False

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    # (0, '퇴출요청'),   >> args 에 URL 삽입
    # (1, '장난금지'),   >> args 에 URL 삽입
    # (2, '동물퇴출'),   >> args 에 URL 삽입
    # (3, '사이렌'),   >> args 에 URL 삽입
    # (4, '냉난방기 켜기'),  >> 디바이스리스트에서 ctrl 리스트 검색해서 키오스크에 전달
    # (5, '장비전원 재시작'),
    # (6, 'PC재부팅')
    # (7, '코인신호보내기') >> args 에  { ctrl_id, coin } 삽입
    # (8, '업그레이드 요청') >> args 에  { file_path } 삽입
    # (9, '서버 업그레이드 요청)
    def run(self):
        
        while not self.stopped():
            time.sleep(30)
            try:
                res = self._handler.do_api('/alert')
                if res.status_code != 200:
                    continue
            except:
                continue
            
            #위 try문에서 db에서 읽어오게되고.
            cmd_list = res.json()
            config = Config()

            # print("cmd_list :{},config : {}".format(cmd_list,config))

            #_isupgrade 가 true가 아니면 여기를 실행. 초기설정이 False로 되어있으니까.
            if self._isupgrade is not True:
                for c in cmd_list:
                    cmd = c.get('cmd', -1)
                    if cmd < 0:
                        continue
                    if cmd < 4 or cmd == 10:
                        print("sever command cmd : {}".format(cmd))
                        args = c.get('args', None)

                        print("sever command args : {}".format(args))

                        wavName=''

                        if(cmd==0):
                            wavName='byebye.wav'
                        elif(cmd==1):
                            wavName='quiet.wav'
                        elif(cmd==2):
                            wavName='pet.wav'
                        elif(cmd==3):
                            wavName='siren.wav'
                        elif(cmd==10):
                            wavName='bayernAlert.wav'

                        if not args:
                            continue
                        url = config.get_config('server').get('url')
                        res_data = requests.get(url + args).content
                        #path = os.path.join(os.path.dirname( #기존코드
                        #os.path.abspath(__file__)), '..', 'bin', 'tmp.wav') #기존코드

                        path = os.path.join(os.path.dirname(
                            os.path.abspath(__file__)), '..', 'bin', wavName)

                        print("sever command url : {}".format(url))
                        # print("sever command res_data : {}".format(res_data))
                        print("sever command path : {}".format(path))

                        print("sever command  wav file open start")
                        with open(path, 'wb') as f:
                            f.write(res_data)
                        winsound.PlaySound(path, winsound.SND_FILENAME)
                        print("sever command  wav file open end")

                    # 업데이트 신호 커맨드 (현재 작업중 )
                    elif cmd == 8:

                        #파라미터 
                        args = c.get('args', None)
                        if not args:
                            continue
                        url = config.get_config('server').get('url')
                        res_data = requests.get(url + args).content
                        base_path = os.path.join(os.path.dirname(
                            os.path.abspath(__file__)), '..') #base_path backend 하위경로
                        path = os.path.join(base_path, 'bin', 'upgrade.zip')

                        print("path : {}".format(path))

                        #static 파일지정 
                        access_denied_path = os.path.join(base_path, 'static', 'access-denied.html')
                        with open(access_denied_path, 'r') as f:
                            f.write(res_data)

                      



                        #실행부분 (분리)


                        # 현재 진행중인 작업기다려주기.(일단 기다려주기코드로 짜놓고 추후생각)

                        # 업그레이드 파일 열기 
                        # with open(path, 'wb') as f:
                        #     f.write(res_data)

                        # z = zipfile.ZipFile(path)
                        # z.extractall(base_path)

                        # time.sleep(5)

                        # #컴퓨터 재부팅
                        # if os.name == 'nt':
                        #     import subprocess
                        #     subprocess.call('shutdown /r /t 0'.split(' '))
                    else:
                        kiosk = KioskHandler()
                        if cmd == 4:
                            device = config.get_config('devices')
                            airdev = device.get('airconditioner', None)
                            if not airdev:
                                continue
                            kiosk.send_coins(1, int(airdev[0]))
                        elif cmd == 5:
                            args = c.get('args', None)
                            if not args:
                                continue
                            try:
                                args = args.replace("'", '"')
                                args = json.loads(args)
                            except:
                                continue
                            if args['onoff'] == 0:
                                kiosk.send_reset(int(args['ctrl_id'])) # 전원리셋
                            elif args['onoff'] == 1:
                                kiosk.send_shutdown(int(args['ctrl_id'])) # 전원Off
                            else:
                                kiosk.send_start(int(args['ctrl_id'])) # 전원On
                                
                        elif cmd == 6:
                            if os.name == 'nt':
                                import subprocess
                                subprocess.call('shutdown /r /t 0'.split(' '))
                        elif cmd == 7:
                            args = c.get('args', None)
                            if not args:
                                continue
                            try:
                                args = args.replace("'", '"')
                                args = json.loads(args)
                            except:
                                continue
                            kiosk.send_coins(
                                int(args['coin']), int(args['ctrl_id']))
                        elif cmd == 9:
                            if not args:
                                continue
                            try:
                                args = c.get('args', None)
                                args = json.loads(args)
                            except:
                                continue
                            kiosk.send_upgrade(int(args['isupgrade']))

# 냉난방기
# "cmd": 4,
# "args": "{'coin': 1, 'ctrl_id': 11}",
if __name__ == "__main__":
    with ServerHandler() as h:
        res = h.do_api('/alert')
        print(res)
        print("sever_command_main 진입")
