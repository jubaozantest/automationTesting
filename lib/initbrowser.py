""" 浏览器初始化
"""
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from util.default_path import get_config
from logs.log import logger
from lib.read_config import read_basic_config as basic
config=get_config()
executable_path=config.WINDOWS_CHROME_DRIVER

class ElementNotFoundException(Exception):
    pass

def supportBrowserType(browsertype, url):
        '''
        设置UI自动化打开游览器的类型，和打开浏览器的url
        参数browsertype:浏览器类型
        参数url：访问页面的url
        :return:返回浏览器对象
        '''

        options = webdriver.ChromeOptions()
        '''谷歌的headless模式'''
        if basic.cfg['browser']['mode'] == 'headless':
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
    '''浏览器初始化类，封装一些常用的方法
    get_element_until_is_visible：等待元素出现
    get_elements_until_is_visible：等待多个相同的元素出现
    click_element：点击元素
    send_keys:元素输入
    element_visible_times：元素在页面出现的次数
    '''
    def __init__(self,  browser,url):
        self.driver = supportBrowserType(browser, url)
        self.driver.implicitly_wait(5)

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
        time = 8
        by,inspect,name=args[0],args[1],args[2]
        # try:
        #     element = WebDriverWait(self.driver, time).until(lambda x: x.find_element(by=by,value=inspect))
        #     return element
        try:
            element = WebDriverWait(self.driver, time).until(EC.visibility_of_element_located((By.XPATH,inspect)))
            #x=EC.element_to_be_clickable((By.XPATH,inspect))

            return element
        except Exception:
            raise ElementNotFoundException("{}元素路径找不到".format(name))
    def get_elements_until_is_visible(self,*args):
        '''
        等待某个元素出现，timeout默认5秒，频率0.5
        :param by:定位方式
        :param inspect:值
        :param element:元素名字
        :return: 元素对象webelement列表
        '''
        time = 5
        by,inspect,name=args[0],args[1],args[2]
        try:
            element = WebDriverWait(self.driver, time).until(lambda x: x.find_elements(by=by,value=inspect))
            return element
        except Exception:
            raise ElementNotFoundException("{}元素路径找不到".format(name))

    def click_element(self,*args):
        '''点击元素'''
        logger.info('开始点击元素:"{0}">>>，路径值为:{1}'.format(args[2],args[1]))
        self.get_element_until_is_visible(*args).click()

    def send_keys(self,*args):
        '''键盘输入'''
        logger.info('开始在元素:"{0}">>>输入:{1}，路径值为:{2}'.format(args[2],args[3],args[1]))
        self.get_element_until_is_visible(*args).send_keys(args[3])


    def element_visible_times(self,*args):
        '''验证元素在页面出现的次数'''
        times=len(self.get_elements_until_is_visible(*args))
        logger.info('元素:"{0}">>>在页面上出现的次数为{1}，路径值为:{2}'.format(args[2],times,args[1]))
        return times
