import unittest, time
from lib.basictestcase import BasicTestCase
from lib.initbrowser import BrowserInit
from util.selenium_public_methods import *
from logs.log import logger
from  util.wrappers import timer
from pages.login_page import LoginPage
class LoginSuite(unittest.TestCase):
    basic = BasicTestCase()
    url = basic.url
    browserName = basic.browser
    username = basic.username
    password = basic.password
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
        self.assertEqual(1, 1)

    def login(self,**kwargs):
        self.browser.send_keys(*LoginPage.username_input,kwargs["name"])
        self.browser.send_keys(*LoginPage.pwd_input,kwargs["pwd"])
        self.browser.click_element(*LoginPage.login_button)


if __name__ == "__main__":
    
    unittest.main()

