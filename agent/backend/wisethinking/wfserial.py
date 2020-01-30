import datetime
import serial

DEBUG = False


class WfSerial():
    """워시프렌즈의 RS-232 보드를 핸들링 하기 위한
    시리얼 통신용 클래스
    """

    def __init__(self, dev, baudrate=9600, bit=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None):
        """시리얼 통신을 위한 클래스 초기화

        Parameters
        ----------
        dev: string (required)
            시리얼 통신을 하기 위한 디바이스의 경로
        bandrate: integer (optional)
            bpn (9600, 19200 등)
        bit: serial에 정의된 값 (optional)
             FIVEBITS, SIXBITS, SEVENBITS, EIGHTBITS
            bit
        parity: serial에 정의된 값 (optional)
                PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
            패리티 타입
        stopbits: serial에 정의된 값 (optional)
                  STOPBITS_ONE, STOPBITS_ONE_POINT_FIVE, STOPBITS_TWO
            stopbit
        timeout: float
            timeout
        """
        self._dev = dev
        self._baudrate = baudrate
        self._bit = bit
        self._parity = parity
        self._stopbits = stopbits
        self._timeout = timeout
        if not DEBUG:
            self._serial = serial.Serial(self._dev, baudrate=self._baudrate, bytesize=self._bit,
                                         parity=self._parity, stopbits=self._stopbits,
                                         timeout=self._timeout)

    def write(self, msg, crlf=False, crc=False):
        """bits에 해당하는 데이터를 전달

        Parameters
        ----------
        msg: string
            메시지
        crlf: boolean
            CR LF를 자동으로 추가할지 여부
        crc: boolean
            CRC를 자동으로 추가할지 여부
        """
        if crlf:
            msg += '\r\n'

        msg = msg.encode('ascii')
        
        if crc:
            tmp = msg[0]
            for _idx in range(1, len(msg)):
                tmp = self._gen_checksum(tmp, msg[_idx])
            print(tmp)
            msg += tmp
        msg += '\x03'.encode('ascii')
        if not DEBUG:
            print('write msg => ', msg)
            self._serial.write(msg)
        else:
            print(msg)

    def read(self, size=None):
        print('Read Start')
        if not DEBUG:
            if size:
                print('Read Size: ', size)
                return self._serial.read(size)
            return self._serial.read()
        else:
            return ''

    def _gen_checksum(self, asc1, asc2):
        if type(asc1) == int:
            _asc1 = asc1
        else:
            _asc1 = ord(asc1)
        if type(asc2) == int:
            _asc2 = asc2
        else:
            _asc2 = ord(asc2)

        return chr(_asc1 ^ _asc2).encode('ascii')

    def is_open(self):
        if not DEBUG:
            return self._serial.is_open
        else:
            return True

    def close(self):
        """연결을 닫음
        """
        if not DEBUG:
            if self._serial.is_open:
                self._serial.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


if __name__ == "__main__":
    # with WfSerial('/dev/cu.usbserial-AH076UZY') as wf:
    #     wf.write('cAcAcA', crlf=True)
    now = datetime.datetime.now()
    t = '{}{}{}{}'.format(now.strftime('%Y%m%d'),
                          now.hour, now.minute, now.second)
