import datetime
import json
import random
import socket
import time
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


def get_current_timestamp():
    """
    获取当前时间，返回10位时间戳
    """
    return int(time.time())


def str_time_to_timestamp(str_time):
    time_array = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    return int(time.mktime(time_array))


def check_json_contains(actual, expect):
        err_msg = ''
        for key, value in expect.items():
            if key not in actual:
                err_msg = '实际结果中未找到"{}"这个Key'.format(key)
                return False, err_msg
            if not value == 'isNotNone':
                if actual[key] != expect[key]:
                    err_msg = '"{0}"这个Key的预期结果是"{1}"，实际结果是"{2}"'.format(key, expect[key], actual[key])
                    print(err_msg)
                    return False,err_msg
            else:
                if not actual[key]:
                    err_msg = '实际结果{}的值为空'.format(key)
                    print(err_msg)
                    return False, err_msg
        return True, err_msg

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
        for key ,value in expect.items():
            if key not in actual:
                err_msg += '实际结果中未找到"{}"这个Key'.format(key)
                return False, err_msg
            if not value=='isNotNone':
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


def count_case_by_single_file(f_path):
    """统计某文件里RF用例数量"""
    sum = 0
    with open(f_path, mode='r', encoding='UTF-8') as f:
        exist_lines = f.readlines()
        is_case_file = False
        for line in exist_lines:
            if line.startswith('*** Test Cases ***'):
                is_case_file = True
                continue
            if is_case_file and not line.startswith('    ') and len(line) > 2:
                print('line:{}'.format(line))
                sum += 1
    return sum


def count_rf_cases(root_dir, case_num=None):
    """统计目录下RF用例总数"""
    if not case_num:
        case_num = 0
    f_d_list = os.listdir(root_dir)

    for f_d in f_d_list:
        if f_d.startswith('.'):
            continue
        f_d_path = os.path.join(root_dir, f_d)
        if os.path.isfile(f_d_path):
            if f_d_path.endswith('.txt') or f_d_path.endswith('.robot'):
                case_num += count_case_by_single_file(f_d_path)
        else:
            case_num = count_rf_cases(f_d_path, case_num)

    return case_num




if __name__ == '__main__':
    # print(get_host_port())
    # print(get_current_time())
    # check_dict = {"a": {"C": "122", "B": {"C": "122", "B": {"kk": 123}}},
    #               "b": [1, 2, [3, 2], {"1": [{}, "2"]}, {"1": "2"}], "c": 2}
    # expect_dict = {"a": {"C": "122", "B": {"B": {"kk": {}}}}, "b": [1, [2, 3], {"1": "2"}], "c": 2}
    # a = {"receiveStatusDesc": "优惠券已放入您的券包"}
    # b = {"receiveStatusDesc": None}
    # s = is_json_contains(a, b)
    # print(s)
    # print(generate_idcard())
    pass
    a={
    "code": 0,
    "message": "操作成功",
    "body": {
        "balance": 28.58,
        "canApply": 25.47,
        "noBanlance": 3.11,
        "isbailMoneyToBalance": False,
        "bailMoney": 0,
        "nick": "焦梓意",
        "headerUrl": "http://thirdwx.qlogo.cn/mmopen/vi_32/3goMib31BRX6g1bQTnhbiagrZYzK8wmgyzdQDJubEEEMTcdZOibYebI5dRYVbHele1eq6rDaFjVOt2YAkMsQ6F2icg/132",
        "currency": "元"
    },
    "timestamp": 1557900966
}
    b={"message":"操作成功","body":{"canApply":"select money from fxydym.fx_angent_extend where agentid=14507854"}}
    x=is_json_contains(a,b)
    print(x)