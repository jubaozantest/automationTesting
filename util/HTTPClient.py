import requests,json,time
from logs.log import logger
from util.operation_excel import Excel
from ruamel import yaml
from util.default_path import get_config
from util.tool import  *

extract_path=get_config().EXTRACT_PATH
METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']
defult_headers = {
        # 'Content-Type':'application/json'
        'Content-Type':'application/x-www-form-urlencoded'
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
            headers["Content-Type"]="application/x-www-form-urlencoded"
            self.session.headers.update(headers)
        else:
            self.session.headers.update(defult_headers)
    def set_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send(self, params=None, data=None,extract=None,count=None, **kwargs):
        if data and isinstance(data,str):
            data=eval(data)
            print(type(data))
            for key, value in data.items():
                print(value,type(value))
                '''转换请求参数里面的变量,例如：152${random_phone},{"com":"c3","agentid":14507427,"mobile":15074652511,"siteId":1122}${md5}'''
                if isinstance(value, str):
                    if '${random_phone}' in value:
                        data[key] = value.split('$')[0]+str(random_phone())
                    elif '${md5}' in value:
                        md5_data=value.split('$')[0]
                        data[key] =md5(json.loads(md5_data))
                    elif value.startswith("select") or value.startswith("update") :
                        data[key]=execute_sql(value)
        response = self.session.request(method=self.method, url=self.url, params=params, data=data, **kwargs)
        response.encoding = 'utf-8'
        logger.info('>>>开始执行第{2}个用例{0} {1}'.format(self.method, self.url,count-1))
        logger.info('>>>请求参数为:{}'.format(data))
        logger.info('>>>请求成功: {0}\n接口响应值为:{1}'.format(response, response.text))
        '''写入响应值到excel表的请求响应值'''
        Excel().write_respone(count,response.text)
        if response.status_code==200 and isinstance(response.text,str):
            response=json.loads(response.text)
            '''提取变量写入yaml文件'''
            if extract in response.keys():
                extract_dict={}
                extract_dict[extract]=response[extract]
                with open(extract_path, "w") as yaml_file:
                    yaml.dump(extract_dict, yaml_file, Dumper=yaml.RoundTripDumper)
                    logger.info(">>>开始提取变量{}值为:{}".format(extract,response[extract]))
                    time.sleep(1.8)
        else:
            raise RequestFailed('请求500')
        return response


if __name__=="__main__":
    pass
