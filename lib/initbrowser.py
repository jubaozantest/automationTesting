# -*- coding: utf-8 -*-
""" 浏览器初始化
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from util.default_path import get_config
from logs.log import logger
from lib.config import test_config
config=get_config()
executable_path=config.WINDOWS_CHROME_DRIVER

class ElementNotFoundException(Exception):
    pass

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
        by,inspect,name=args[0],args[1],args[2]
        try:
            element = WebDriverWait(self.driver, time).until(lambda x: x.find_element(by=by,value=inspect))
            return element
        except Exception:
            raise ElementNotFoundException("{}元素路径找不到".format(name))
    def click_element(self,*args):
        logger.info('开始点击元素:{0}，路径值为:{1}'.format(args[2],args[1]))
        self.get_element_until_is_visible(*args).click()

    def send_keys(self,*args):
        logger.info('开始在元素:{0}输入:{1}，路径值为:{2}'.format(args[2],args[3],args[1]))
        self.get_element_until_is_visible(*args).send_keys(args[3])
