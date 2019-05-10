from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException, NoAlertPresentException, \
    NoSuchWindowException, NoSuchFrameException
from selenium.webdriver.support.wait import WebDriverWait


def is_alert_present(driver):
    '''
    处理alert弹窗
    :param self:
    :param driver:
    :return:
    '''
    try:
        alert = driver.switch_to.alert
        return alert
    except:
        raise NoAlertPresentException


def execute_javascript(driver, js):
    '''
    执行js:js= 'window.open("https://www.baidu.com")'
    :param driver:
    :param js:
    :return:
    '''
    try:
        driver.execute_script(js)
    except Exception:
        raise NoSuchAttributeException


def operate_elements(driver, how, inspect):
    '''
    操作元素方法：id、name、classname、xpath、tagname、linktext、cssSelector
    :param driver:
    :param how:
    :param inspect:
    :return:
    '''
    try:
        ele = driver.find_element(by=how, value=inspect)
        return ele
    except:
        raise NoSuchElementException


def get_element_until_is_visible(driver,*args):
    '''
    等待某个元素出现，timeout默认5秒，频率0.5
    :param by:定位方式
    :param inspect:值
    :param element:元素名字
    :return: 元素对象webelement
    '''
    time = 5
    try:
        element = WebDriverWait(driver, time).until(lambda x: x.find_element(*args))
        return element
    except Exception:
        raise ("{0}元素路径找不到")


def wait_until_element_is_visible_mobile(driver, by, inspect, input_value):
    '''
    等待某个元素出现，timeout10秒，频率0.5
    :param by:
    :param value:
    :return:
    '''
    element = ''
    try:
        if not inspect == 'common':
            driver.implicitly_wait(5.0)
            if by == 'id':
                element = driver(resourceId=inspect)
            elif by == "text":
                element = driver(text=inspect)
            elif by == "xpath":
                element = driver.xpath(inspect)
            elif by == "classname":
                element = driver(className=inspect)
        else:
            driver.implicitly_wait(5.0)
            if by == "text":
                element = driver(text=input_value)
            elif by == "xpath":
                element = driver.xpath("//*[@text='{}']".format(input_value))
        return element
    except:
        raise ("{}元素未找到".format(inspect))


def wait_until_element_is_notvisible(driver, by, value):
    '''
    等待某个元素消失，timeout10秒，频率0.5
    :param by:
    :param value:
    :return:
    '''
    time = 10
    try:
        is_present = WebDriverWait(driver, time).until_not(
            lambda x: x.find_element(by=by, value=value).is_displayed())
        return is_present
    except:
        raise NoSuchElementException


def switch_to_handle(driver, index):
    '''
    切换窗口句柄
    :param driver:
    :param index:
    :return:
    '''
    try:
        handle_list = driver.windwo.handles
        driver.switch_to.handle(handle_list[index])
    except:
        raise NoSuchWindowException


def switch_to_frame(driver, frame):
    '''
    切换framework
    :param driver:
    :param frame:
    :return:
    '''
    try:
        driver.switch_to.frame(frame)
    except:
        raise NoSuchFrameException

# def move_to_element(driver, ele):
#     '''
#     鼠标移动
#     :param driver:
#     :param tag:
#     :return:
#     '''
#     try:
#         ActionChains(driver).move_to_element(ele).perform()
#     except:
#         raise NoSuchElementException
