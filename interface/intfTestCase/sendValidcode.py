import unittest,time,json,requests
from interface.HTTPClient import HTTPClient
from logs.log import logger
from util.default_path import get_config
config = get_config()


class GetMenuHTTP(unittest.TestCase):
    URL = 'https://trade.jubaozan.cn/micro/merchant-api/merchant/menu/getMenu'
    payload = {}
    data=json.dumps(payload)

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='POST')

    def test_getMenu(self):
        res = self.client.send(data=self.data)
        logger.info(res.text)


if __name__ == '__main__':

    unittest.main()


