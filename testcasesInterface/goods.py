'''
商品接口
'''
import unittest
from util.HTTPClient import HTTPClient
from lib.config import test_config
from ddt import ddt,data

@ddt
class GoodsPoster(unittest.TestCase):
    URL = test_config.interface_pre + 'auth/login'
    # testdata=[{"params":{"mobile": "15202127953", "siteId": 1123, "loginType": 1, "validCode": 1482},
    #            "checkpoint":{"success":True,"token":"isNotNone"}}]

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='POST')

    @data(*testdata)
    def test_right_numIid(self,tdata):
        '''
        正确的商品id
        :return:
        '''
        res = self.client.send(data=tdata["params"])
        print("tdata['checkpoint']",tdata['checkpoint'])
        self.assertEqual(res['success'], tdata['checkpoint']['success'])
        self.assertIsNotNone(res['token'])
        return res['token']



if __name__ == '__main__':
    unittest.main()
