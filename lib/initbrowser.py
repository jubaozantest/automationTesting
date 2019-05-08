# -*- coding: utf-8 -*-
""" 浏览器初始化
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from util.default_path import get_config
from lib.config import test_config
config=get_config()
executable_path=config.WINDOWS_CHROME_DRIVER

def supportBrowserType(browsertype, url):
        '''
        设置需要使用的浏览器及浏览器配置,并打开指定页面
        browsertype:浏览器类型
        url：访问页面的url
        '''

        options = webdriver.ChromeOptions()
        if test_config.cfg['browser']['mode'] == 'headless':
            options.add_argument("headless")

        options.add_argument("start-maximized")

        if browsertype is None:
            raise WebDriverException("浏览器类型不能为空")
            #self.skipTest("请指定所使用的浏览器")
        if browsertype == 'ie':
            browser = webdriver.Ie()
        elif browsertype == 'firefox':
            browser = webdriver.Firefox()
        elif browsertype == 'chrome':
            browser = webdriver.Chrome(options=options,executable_path=executable_path)
        else:
            raise WebDriverException("暂无支持%s浏览器类型", browsertype)
            #self.skipTest("暂无支持%s浏览器类型", browsertype)
        browser.get(url)
        browser.fullscreen_window()
        return browser

class BrowserInit(object):
    def __init__(self,  browser,url):
        self.driver = supportBrowserType(browser, url)
    def quit(self):
        return self.driver.quit()

    def get_element_until_is_visible(self,*args):
        '''
        等待某个元素出现，timeout默认5秒，频率0.5
        :param by:定位方式
        :param inspect:值
        :param element:元素名字
        :return: 元素对象webelement
        '''
        time = 5
        try:
            element = WebDriverWait(self.driver, time).until(lambda x: x.find_element(*args))
            return element
        except Exception:
            raise ("{0}元素路径找不到")


# class BrowserConfig(object):
#     '''
#     设置需要使用的浏览器及浏览器配置
#     '''
#     def __init__(self):
#         pass
#
#     def setbrowser(self, browsertype, url):
#
#         '''
#         设置需要使用的浏览器及浏览器配置,并打开指定页面
#         browsertype:浏览器类型
#         url：访问页面的url
#         '''
#
#         options = webdriver.ChromeOptions()
#         if test_config.cfg['browser']['mode'] == 'headless':
#             options.add_argument("headless")
#
#         options.add_argument("start-maximized")
#
#         if browsertype is None:
#             raise WebDriverException("浏览器类型不能为空")
#             #self.skipTest("请指定所使用的浏览器")
#         if browsertype == 'ie':
#             self.browser = webdriver.Ie()
#         elif browsertype == 'firefox':
#             self.browser = webdriver.Firefox()
#         elif browsertype == 'chrome':
#             self.browser = webdriver.Chrome(options=options)
#         else:
#             raise WebDriverException("暂无支持%s浏览器类型", browsertype)
#             #self.skipTest("暂无支持%s浏览器类型", browsertype)
#         self.browser.get(url)
#         #self.browser.fullscreen_window()
#         return self.browser
#
# def browserInstance(browser,url):
#     return BrowserConfig().setbrowser(browser,url)
