import unittest, time
from lib.basictestcase import BasicTestCase
from lib.initbrowser import BrowserInit
from util.wrappers import timer
from pages.login_page import LoginPage
from pages.shouye import ShouYe
from pages.yingxiao import ManJianManSong


class ManJianManSongSuite(unittest.TestCase):
    basic = BasicTestCase()
    url = basic.url
    browserName = basic.browser
    username = basic.username
    password = basic.password

    @classmethod
    def setUpClass(self):
        '''浏览器设置'''

        self.browser = BrowserInit(self.browserName, self.url)

    # @classmethod
    # def tearDownClass(self):
    #     "关闭浏览器"
    #     self.browser.quit()

    @timer
    def test_1_add_manjianmansong(self):
        '''
        用例1：正确的用户登录
        :return:
        '''
        self.login(name=self.username, pwd=self.password)
        self.browser.click_element(*ShouYe.yingxiao)
        self.browser.click_element(*ManJianManSong.manjianmansong_link)
        time.sleep(3)
        self.browser.click_element(*ManJianManSong.add_button)
        time.sleep(5)
        self.browser.send_keys(*ManJianManSong.huodongmingcheng_input,'hjhtest')
        self.browser.click_element(*ManJianManSong.shengxiaoshijian_input)
        self.browser.click_element(*ManJianManSong.kaishishijian)
        self.browser.click_element(*ManJianManSong.jiesushijian)
        self.browser.click_element(*ManJianManSong.confirm)
        self.browser.send_keys(*ManJianManSong.youhuishezhi_input,'10')
        self.browser.click_element(*ManJianManSong.jianxianjin_radio)
        self.browser.send_keys(*ManJianManSong.jianxianjin_input,'2')
        self.browser.click_element(*ManJianManSong.baocun_button)


    def login(self, **kwargs):
        self.browser.send_keys(*LoginPage.username_input, kwargs["name"])
        self.browser.send_keys(*LoginPage.pwd_input, kwargs["pwd"])
        self.browser.click_element(*LoginPage.login_button)


if __name__ == "__main__":
    unittest.main()


