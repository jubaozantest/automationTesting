import unittest,time
from util.HTTPClient import HTTPClient
from lib.config import test_config,extract_config
from util.operation_excel import Excel
from ddt import ddt,data
from util.tool import is_json_contains
row=1
@ddt
class AuthLogin(unittest.TestCase):
    testdata=Excel().read_excel()
    def setUp(self):
        pass
        #self.client = HTTPClient(url=self.URL, method='POST')

    @data(*testdata)
    def test_cases(self,tdata):
        global row
        row+=1
        headers,params,url,method,checkkpoint=tdata['请求头信息'],tdata['请求入参'],tdata['接口url'],tdata['请求方式'],tdata['检查点']
        extract=tdata['提取变量']
        '''替换头部信息包含上个接口提取的变量'''
        if headers:
            headers = eval(headers)
            for key, value in headers.items():
                if value.startswith("{{") and value.endswith("}}"):
                    value = value.split("{{")[1].split("}}")[0]
                    replace = extract_config.extract(value)
                    headers[key]=replace
        client = HTTPClient(url=url, method=method,headers=headers)
        res = client.send(data=params,extract=extract,count=row)
        '''校验excel中的检查点：1.字段的值和respone中的值相等 2.字段的值不为空'''
        if checkkpoint:
            checkkpoint = eval(checkkpoint)
            result=is_json_contains(res,checkkpoint)
            Excel().write_result(row,result[0])
            self.assertTrue(result[0],result[1])
if __name__ == '__main__':
    unittest.main()
