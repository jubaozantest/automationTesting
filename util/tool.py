import datetime
import json
import random
import socket
import time
import hashlib

import os
from util.query_mysql import execute_sql

def get_host():
    """
    获取运行主机host
    :return:
    """
    ip = socket.gethostbyname(socket.gethostname())
    return str(ip)


def get_host_port():
    """
    获取运行主机host+port
    :return:
    """
    ip = get_host()
    return "{}:7000".format(ip)
    # return "99.48.58.31:7000"


def get_current_time():
    """
    获取当前时间，返回YYYY-mm-dd HH:MM:SS格式的时间字符串
    """
    return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

def random_phone():
    return random.randrange(0, 99999999)

def generate_phone(top=None):
    if not top:
        phone_list = ['136', '188', '134', '135', '184', '187', '183']  # 定义号码段
        phone = random.choice(phone_list) + "".join(random.choice("0123456789") for _ in range(8))
    else:
        phone = str(top) + "".join(random.choice("0123456789") for _ in range(8))
    return phone


def get_current_timestamp():
    """
    获取当前时间，返回10位时间戳
    """
    return int(time.time())


def str_time_to_timestamp(str_time):
    time_array = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(time_array))



def is_json_contains(actual, expect, err_msg=''):
    if not isinstance(actual, (list, dict)):
        err_msg += '实际结果不是Json格式'
        return False, err_msg
    if not isinstance(expect, (list, dict)):
        err_msg += '预期结果不是Json格式'
        return False, err_msg
    if not isinstance(actual, type(expect)):
        err_msg += '预期结果和实际结果的数据类型不同，预期结果的类型是"{0}"，实际结果的类型是"{1}"'.format(
            type(expect).__name__, type(actual).__name__)
        return False, err_msg
    if isinstance(actual, list) and isinstance(expect, list):
        actual_inner_dict_list = []
        actual_inner_list_list = []
        for key in actual:
            if isinstance(key, dict):
                actual_inner_dict_list.append(key)
            elif isinstance(key, list):
                actual_inner_list_list.append(key)
        for key in expect:
            if isinstance(key, dict):
                flag = False
                for _key in actual_inner_dict_list:
                    if is_json_contains(_key, key, err_msg) is True:
                        flag = True
                if not flag:
                    return False
            elif isinstance(key, list):
                flag = False
                for _key in actual_inner_list_list:
                    if is_json_contains(_key, key, err_msg) is True:
                        flag = True
                if not flag:
                    return False
            elif key not in actual:
                return False
    elif isinstance(actual, dict) and isinstance(expect, dict):
        for key, value in expect.items():
            if isinstance(value,str):
                value=value.upper()
            if key not in actual:
                err_msg += '实际结果中未找到"{}"这个Key'.format(key)
                return False, err_msg
            if not value=='ISNOTNONE':
                # if not isinstance(actual[key], type(expect[key])):
                #     err_msg += '"{0}"这个Key的预期结果类型是"{1}",实际结果类型是"{2}"'.format(
                #         key, type(expect[key]).__name__, type(actual[key]).__name__)
                #     return False, err_msg
                if isinstance(actual[key], dict) and isinstance(expect[key], dict):
                    res = is_json_contains(actual[key], expect[key], err_msg)
                    if res is not True:
                        return res
                elif isinstance(actual[key], list) and isinstance(expect[key], list):
                    res = is_json_contains(actual[key], expect[key], err_msg)
                    if res is not True:
                        return res
                '''数据库校验'''
                if isinstance(expect[key],str) and expect[key].startswith("select") :
                    expect[key]=execute_sql(expect[key])
                    if actual[key] != expect[key]:
                        err_msg += '"{0}"这个Key的预期结果是"{1}"，实际结果是"{2}"'.format(key, expect[key], actual[key])
                        return False, err_msg
                elif actual[key] != expect[key]:
                    err_msg += '"{0}"这个Key的预期结果是"{1}"，实际结果是"{2}"'.format(key, expect[key], actual[key])
                    return False, err_msg
            else:
                if not actual[key]:
                    err_msg = '实际结果{}的值为空'.format(key)
                    return False, err_msg
    return True,err_msg


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.__str__()
        return json.JSONEncoder.default(self, obj)


def json_dumps(dic):
    return json.dumps(dic, ensure_ascii=False, cls=DateEncoder)


def json_loads(str_):
    return json.loads(str_)

def json_phone():
    return random.randrange(0, 99999999)

def generate_random_num(min_, max_):
    return random.randint(min_ + 1, max_)


def generate_idcard():
    """
生成身份证号，生成规则同真实身份证，18位，最后一位可以是数字或者X
    :return:身份证号
    """
    ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')

    u''' 随机生成新的18为身份证号码 '''
    t = time.localtime()[0]

    first_list = ['362402', '362421', '362422', '362423', '362424', '362425', '362426', '362427', '362428', '362429',
                  '362430', '362432', '110100', '110101', '110102', '110103', '110104', '110105', '110106', '110107',
                  '110108', '110109', '110111', '320101', '320102', '320103', '320104', '320105', '320106']

    x = '%06d%04d%02d%02d%03d' % (int(random.choice(first_list)),
                                  random.randint(t - 50, t - 19),
                                  random.randint(1, 12),
                                  random.randint(1, 28),
                                  random.randint(1, 999))

    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    id_card = '%s%s' % (x, LAST[y % 11])
    return id_card

def md5(data):
    string = json.dumps(data).replace(': ', ':').replace(', ', ',')
    m = hashlib.md5()
    m.update(string.encode(encoding='utf-8'))
    return m.hexdigest()

if __name__ == '__main__':
    data={"com":"c3","agentid":14507967,"mobile":18973195297,"siteId":1122}
    print(md5(data))
    print(generate_phone(152))
