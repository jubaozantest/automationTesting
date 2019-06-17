import unittest,time
from util.HTTPClient import HTTPClient
from lib.read_config import read_basic_config,read_extract_config
from util.operation_excel import Excel
from ddt import ddt,data
from util.tool import is_json_contains
import warnings

row=1          #统计用例个数
sheet_index=0  #计算sheet个数
@ddt
class AuthLogin(unittest.TestCase):
    excel_data=Excel().read_excel()
    case_data=excel_data[0] #用例信息列表
    excel_data=excel_data[1] #excel表格sheet个数

    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        #self.client = HTTPClient(url=self.URL, method='POST')

    @data(*case_data)
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
            host = read_basic_config.variables(value)
        url=host+apiUrl
        '''解析headers,替换头部信息包含上个接口提取的变量,例如{{token}}'''
        if headers:
            headers = eval(headers)
            for key, value in headers.items():
                if isinstance(value,str) and value.startswith("{{") and value.endswith("}}"):
                    value = value.split("{{")[1].split("}}")[0]
                    replace = read_extract_config.extract(value)
                    headers[key]=replace
                elif isinstance(value,str) and value.startswith("{") and value.endswith("}"):
                    value = value.split("{")[1].split("}")[0]
                    replace = read_basic_config.variables(value)
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

