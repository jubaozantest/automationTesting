
import os
import platform

from util.tool import get_host


class Config(object):

    # 获取文件目录相对路径
    BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')

    JSON_AS_ASCII = False
    # SECRET_KEY = os.urandom (24)

    # mysql
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_TEARDOWN = True
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_POOL_TIMEOUT = 20
    SQLALCHEMY_POOL_RECYCLE = 900


    LINUX_BASE_PATH = '/usr/local/src/atp'

    # log
    LINUX_LOG = '/usr/local/src/logs/atp-auto-core/atp-auto-core.log'
    # WINDOWS_LOG = r'E:\git_mime\atp-platform-core\atp\logs\flask.log'
    WINDOWS_LOG =BASE_PATH + r'\logs' + r'\selenium.log'


    # reports dir
    LINUX_REPORT_DIR = LINUX_BASE_PATH + '/reports/'
    WINDOWS_REPORT_DIR = BASE_PATH + r'\reports'

    #chromedriver
    LINUX_CHROME_DRIVER=LINUX_BASE_PATH+'drivers'
    WINDOWS_CHROME_DRIVER=BASE_PATH+ r'\driver\chromedriver.exe'

    #extract
    LINUX_EXTRACT=LINUX_BASE_PATH+'drivers'
    WINDOWS_EXTRACT=BASE_PATH+ r'\config\extract.yaml'
    # extract
    LINUX_CONFIG = LINUX_BASE_PATH + 'drivers'
    WINDOWS_CONFIG = BASE_PATH + r'\config\config.yaml'

    if platform.system() == 'Linux':
        LOG_PATH = LINUX_LOG

        REPORT_DIR = LINUX_REPORT_DIR

    elif platform.system() == 'Windows':

        LOG_PATH = WINDOWS_LOG
        REPORT_DIR = WINDOWS_REPORT_DIR
        EXTRACT_PATH=WINDOWS_EXTRACT
        WINDOWS_CONFIG=WINDOWS_CONFIG

    else:
        LOG_PATH = LINUX_LOG

        REPORT_DIR = LINUX_REPORT_DIR
    # email to
    EMAIL_TO = []



    # login_expire_time
    LOGIN_EXPIRE_TIME = 28800  # 8 hours



def get_config():
    return Config


if __name__ == '__main__':
    print(os.path.split(os.path.realpath(__file__))[0])
