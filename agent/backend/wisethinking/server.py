import requests
from wisethinking.config import Config


class ServerHandler():
    """서버를 다루는 상위클래스
    """

    def __init__(self, host=None):
        """서버 클래스 생성자
        """
        _config = Config()
        self._config = _config.get_config('server')

        if host:
            self._host = host
        else:
            self._host = self._config.get('url')

        self._token = _config.get_config('agency').get('seckey', '')

    def is_correct_keys(self, kid, seckey):
        data = {
            'kid': kid,
            'seckey': seckey
        }
        res = requests.post(
            '{}/api/wafos/init-check'.format(self._host), data=data)
        if res.status_code == 200:
            return True
        else:
            return False

    def do_api(self, uri, data=None, reqtype='GET'):
        """서버에 API를 전달

        Paramenters
        -----------
        uri: string
            API를 전달할 URI
        data: dictionary (optional)
            전달할 데이터
        reqtype: string (GET, POST, PUT)
            사용할 HTTP 메소드

        Return
        ------
        response (requests object)

        """

        if not self._token:
            raise NotImplementedError('No token')

        res = None
        headers = {
            'Authorization': self._token
        }
        if reqtype.upper() == 'GET':
            res = requests.get('{}/api/wafos{}'.format(self._host, uri),
                               data=data, headers=headers)
        elif reqtype.upper() == 'POST':
            res = requests.post('{}/api/wafos{}'.format(self._host, uri),
                                data=data, headers=headers)
        elif reqtype.upper() == 'PUT':
            res = requests.put('{}/api/wafos{}'.format(self._host, uri),
                               data=data, headers=headers)
        else:
            raise NotImplementedError('No supported method')

        # print(res.text) #기존구문

        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return


if __name__ == "__main__":
    with ServerHandler() as http:
        http.do_api('/test')
