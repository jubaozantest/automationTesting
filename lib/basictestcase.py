""" 基础类
"""

import unittest, time, re
from selenium.webdriver.support.ui import Select
from lib.config import test_config

class BasicTestCase(object):
    browser = test_config.browser_name
    url = test_config.server
    username = test_config.cfg['user01']['name']
    password = test_config.cfg['user01']['password']
    def __init__(self):
        pass

    def setUp(self):
        "初始化测试用例"



