import requests, json, time
from logs.log import logger
from util.operation_excel import Excel
from ruamel import yaml
from util.default_path import get_config
from util.tool import *

extract_path = get_config().EXTRACT_PATH
METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']
extract_dict = {}
defult_headers = {
    # 'Content-Type':'application/json'
    'Content-Type': 'application/x-www-form-urlencoded'
    # 'Content-Type':'multipart/form-data'
}


class UnSupportMethodException(Exception):
    pass


class RequestFailed(Exception):
    pass


class HTTPClient(object):
    def __init__(self, url, method='GET', headers=None, cookies=None):
        self.url = url
        self.session = requests.session()
        self.method = method.upper()
        if self.method not in METHODS:
            raise UnSupportMethodException('不支持的method:{0}，请检查传入参数！'.format(self.method))

        self.set_headers(headers)
        self.set_cookies(cookies)

    def set_headers(self, headers):
        if headers:
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            self.session.headers.update(headers)
        else:
            self.session.headers.update(defult_headers)

    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def analysis_data(self,data):
        params = eval(data)
        for key, value in params.items():
            '''转换请求参数里面的变量,例如：152${random_phone},{"com":"c3","agentid":14507427,"mobile":15074652511,"siteId":1122}${md5}'''
            if isinstance(value, str):
                if '${random_phone}' in value:
                    params[key] = str(generate_phone(value.split('$')[0]))
                elif '${md5}' in value:
                    md5_data = value.split('$')[0]
                    params[key] = md5(json.loads(md5_data))
                elif value.startswith("select") or value.startswith("SELECT") or value.startswith("update"):
                    params[key] = execute_sql(value)
        return  params
    def send(self, params=None, data=None, extract=None, count=None, sheet_index=None, **kwargs):
        if data and isinstance(data, str):
            data = self.analysis_data(data)
        if params and isinstance(params, str):
            params=self.analysis_data(params)
        response = self.session.request(method=self.method, url=self.url, params=params, data=data, **kwargs)
        response.encoding = 'utf-8'
        logger.info('>>>开始执行第{3}个表格的第{2}个用例{0} {1}'.format(self.method, self.url, count - 1, sheet_index + 1))
        logger.info('>>>请求参数为:{0}{1}'.format(data, params))
        logger.info('>>>请求成功: {0}\n接口响应值为:{1}'.format(response, response.text))
        '''写入响应值到excel表的请求响应值'''
        Excel().write_respone(sheet_index, count, response.text)
        if response.status_code == 200 and isinstance(response.text, str):
            response = json.loads(response.text)
            '''提取变量写入yaml文件'''
            if extract:
                variable_name = extract.split("=")[0]
                extract_name = extract.split("=")[1]
                if extract_name in response.keys():
                    extract_dict[variable_name] = response[extract_name]
                    with open(extract_path, "w") as yaml_file:
                        yaml.dump(extract_dict, yaml_file, Dumper=yaml.RoundTripDumper)
                        logger.info(
                            ">>>开始提取变量{0}值为:{1},提取后的名称为{2}".format(extract_name, response[extract_name], variable_name))
                time.sleep(1.8)
        else:
            raise RequestFailed('请求500')
        return response


if __name__ == "__main__":
    pass
    extract_dict = {"token1": "123",
                    "token2": "456",
                    "token3": "789"}
    with open(extract_path, "w") as yaml_file:
        yaml.dump(extract_dict, yaml_file, Dumper=yaml.RoundTripDumper)
