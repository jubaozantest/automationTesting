import unittest, time
from lib.initbrowser import BrowserInit
from logs.log import logger
from  util.wrappers import timer
from pages.login_page import LoginPage
from lib.read_config import read_basic_config as basic
class LoginSuite(unittest.TestCase):
    '''登录模块的测试用例，
        先从config.yaml获取：UI自动化打开浏览器的url，浏览器的名称，用户名等信息
    '''
    url = basic.server
    browserName = basic.browser_name
    username = basic.cfg['user01']['name']
    password = basic.cfg['user01']['password']
    @classmethod
    def setUpClass(self):
        '''浏览器设置'''
        self.browser=BrowserInit(self.browserName,self.url)
    @classmethod
    def tearDownClass(self):
        "关闭浏览器"
        self.browser.quit()

    @timer
    def test_1_correct_user(self):
        '''
        用例1：正确的用户登录
        :return:
        '''
        self.login(name=self.username, pwd=self.password)
        times=self.browser.element_visible_times(*LoginPage.shouye,)
        self.assertEqual(times,1)

    def login(self,**kwargs):
        '''登录通用方法'''
        self.browser.send_keys(*LoginPage.username_input,kwargs["name"])
        self.browser.send_keys(*LoginPage.pwd_input,kwargs["pwd"])
        self.browser.click_element(*LoginPage.login_button)

if __name__ == "__main__":
    unittest.main()

