'''
手机号登录接口
'''
import unittest
from interface.HTTPClient import HTTPClient
from lib.config import test_config

class Login(unittest.TestCase):
    URL =test_config.interface_pre+ 'auth/login'
    headers={
        'Content-Type':'application/x-www-form-urlencoded'
    }
    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='POST',headers=self.headers)

    def test_validCode_login(self):
        '''
        152验证码登录，
        :return:
        '''
        payload = {"mobile": "15202127953", "siteId": 1123, "loginType": 1, "validCode": 1482}
        res = self.client.send(data=payload)
        print(res.text,type(res.text))
        print(res.content,type(res.content))
    def test(self):
        '''

        :return:
        '''

if __name__ == '__main__':
    unittest.main()


