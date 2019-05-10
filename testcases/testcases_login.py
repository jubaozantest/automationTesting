import unittest, time
from lib.basictestcase import BasicTestCase
from lib.initbrowser import BrowserInit
from util.selenium_public_methods import *
from logs.log import logger
from  util.wrappers import timer
from pages.login_page import LoginPage
from pages.linshou_shouyishezhi import Linshou
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
        self.browser.get_element_until_is_visible(*LoginPage.username_input).send_keys(kwargs["name"])
        self.browser.get_element_until_is_visible(*LoginPage.pwd_input).send_keys(kwargs["pwd"])
        self.browser.get_element_until_is_visible(*LoginPage.login_button).click()

    def test_2_bujifenyong(self):
        self.browser.get_element_until_is_visible(*Linshou.linshoutab).click()
        self.browser.get_element_until_is_visible(*Linshou.tianjiachanpinbutton).click()

if __name__ == "__main__":
    unittest.main()

