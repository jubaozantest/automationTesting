import unittest,time,json,requests
from interface.HTTPClient import HTTPClient
from logs.log import logger
from lib.HTMLTestRunner_hjh import HTMLTestRunner
from util.default_path import get_config
config = get_config()
now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
report_path = config.REPORT_DIR+r'\{0}-intf-report.html'.format(now)


class GetMenuHTTP(unittest.TestCase):
    # URL = Config().get('URL')
    URL = 'https://trade.jubaozan.cn/micro/merchant-api/merchant/menu/getMenu'
    payload = {}
    data=json.dumps(payload)
    headers={
        'Content-Type': "application/json",
        'x-c3-token':"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTc2NTI3NDIxMDcsInBheWxvYWQiOiJ7XCJrZXlUeXBlXCI6XCJ1c2VyaWRcIixcInVzZXJLZXlcIjpcInNqc2RtelwiLFwibWVyY2hhbnRJZFwiOlwiMTEyMlwiLFwic3RvcmVSZWdpb25JZFwiOm51bGwsXCJ1c2VyVHlwZVwiOlwiMVwiLFwiZXhwaXJlXCI6NjA0ODAwMDAwLFwib3RoZXJcIjpudWxsLFwidG9rZW5UaW1lXCI6MTU1NzA0Nzk0MjEwN30ifQ.3FJHrp0YvuMV6UAL_gKh8OOha3fUWTF2yhgbAm-il18"
    }
    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='POST',headers=self.headers)

    def test_getMenu(self):
        res = self.client.send(data=self.data)
        logger.info(res.text)


if __name__ == '__main__':
    # with open(report_path, 'wb') as f:
    #     runner = HTMLTestRunner(f, verbosity=2, title='接口测试用例', description='接口html报告')
    #     runner.run(TestBaiDuHTTP('test_baidu_http'))
    unittest.main()


