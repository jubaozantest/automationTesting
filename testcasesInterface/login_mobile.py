'''
手机号登录接口
'''
import unittest,time
from util.HTTPClient import HTTPClient
from lib.config import test_config



class AuthLogin(unittest.TestCase):
    URL = test_config.interface_pre + 'auth/login'

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='POST')

    def test_validCode(self):
        '''
        152验证码登录，登录成功
        :return:返回token
        '''
        payload = {"mobile": "15202127953", "siteId": 1123, "loginType": 1, "validCode": 1482}
        res = self.client.send(data=payload)
        self.assertEqual(res['success'], True, "请求失败")
        self.assertIsNotNone(res['token'])
        return res['token']

    def test_wrong_user(self):
        '''
        不存在的用户，手机号登录，
        :return:
        '''
        payload = {"mobile": "18374451965", "siteId": 1123, "loginType": 2, "password": 111111}
        res = self.client.send(data=payload)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['errorMessage'],'用户不存在')

    def test_正确的用户(self):
        '''
        不存在的用户，手机号登录，
        :return:
        '''
        payload = {"mobile": "18374451965", "siteId": 1123, "loginType": 2, "password": 111111}
        res = self.client.send(data=payload)
        self.assertEqual(res['success'], False)
        self.assertEqual(res['errorMessage'],'用户不存在')
if __name__ == '__main__':
    unittest.main()
