import unittest,time
from util.HTTPClient import HTTPClient
from lib.config import test_config,extract_config
from util.operation_excel import Excel
from ddt import ddt,data
from util.tool import is_json_contains
import warnings

row=1
sheet_index=0
@ddt
class AuthLogin(unittest.TestCase):
    excel_data=Excel().read_excel()
    testdata=excel_data[0]
    excel_data=excel_data[1]

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        #self.client = HTTPClient(url=self.URL, method='POST')

    @data(*testdata)
    def test_cases(self,tdata):
        global row
        global sheet_index
        if row <self.excel_data[sheet_index]+1:
            row+=1
        else:
            row=2
            sheet_index+=1
        headers,params,apiUrl,method,checkkpoint,host=tdata['请求头信息'],tdata['请求入参'],tdata['接口url'],tdata['请求方式'],tdata['检查点'],tdata["Host"]
        extract=tdata['提取变量']
        '''解析host,如有变量就替换，例如{host}'''
        if isinstance(host,str) and host.startswith("{") and host.endswith("}"):
            value = host.split("{")[1].split("}")[0]
            host = test_config.variables(value)
        url=host+apiUrl
        '''解析headers,替换头部信息包含上个接口提取的变量,例如{{token}}'''
        if headers:
            headers = eval(headers)
            for key, value in headers.items():
                if isinstance(value,str) and value.startswith("{{") and value.endswith("}}"):
                    value = value.split("{{")[1].split("}}")[0]
                    replace = extract_config.extract(value)
                    headers[key]=replace
                elif isinstance(value,str) and value.startswith("{") and value.endswith("}"):
                    value = value.split("{")[1].split("}")[0]
                    replace = test_config.variables(value)
                    headers[key] = str(replace)
        '''开始请求接口，返回接口响应值'''
        client = HTTPClient(url=url, method=method,headers=headers)
        if method=='get' or method=='delete':
            res = client.send(params=params,extract=extract,count=row,sheet_index=sheet_index)
        else:
            res = client.send(data=params,extract=extract,count=row,sheet_index=sheet_index)
        '''校验excel中的检查点：1.字段的值和respone中的值相等 2.字段的值不为空'''
        if checkkpoint:
            try:
                checkkpoint = eval(checkkpoint)
            except NameError:
                from logs.log import logger
                logger.info('!!!!!预期结果不是Json格式!!!!!')
            result=is_json_contains(res,checkkpoint)
            Excel().write_result(sheet_index,row,result[0])
            Excel().write_fail_message(sheet_index,row,result[1])
            #Excel().write_number(row)
            self.assertTrue(result[0],result[1])
if __name__ == '__main__':
    unittest.main()
    # import requests,json
    # headers={
    #         'Content-Type': 'application/x-www-form-urlencoded',
    #         "x-c3-site": "1122",
    #         "x-c3-token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NTk2MzI4Mzc1ODcsInBheWxvYWQiOiJ7XCJrZXlUeXBlXCI6XCJ1c2VyaWRcIixcInVzZXJLZXlcIjpcIjE0NTA3NjY0XCIsXCJtZXJjaGFudElkXCI6XCIxMTIyXCIsXCJzdG9yZVJlZ2lvbklkXCI6bnVsbCxcInVzZXJUeXBlXCI6bnVsbCxcImV4cGlyZVwiOjYwNDgwMDAwMCxcIm90aGVyXCI6bnVsbCxcInRva2VuVGltZVwiOjE1NTkwMjgwMzc1ODd9In0.m49qQJ2Z3ogJmw_JdctlImDRHslgusBsY0S7YDaKtwk"
    #     }
    # data={"shopCartIdJson":[36,37,38,39,40]}
    # da=json.dumps(data)
    # res=requests.request(method='delete',url='https://trade.jubaozan.cn/mall/shopCart/goods',headers=headers,params=data)
    # print(res,res.text)
