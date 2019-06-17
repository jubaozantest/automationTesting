
import os
import platform



class Config(object):

    # 获取文件目录相对路径
    BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')




    # log
    WINDOWS_LOG =BASE_PATH + r'\logs' + r'\selenium.log'


    # reports dir
    WINDOWS_REPORT_DIR = BASE_PATH + r'\reports'

    #chromedriver
    WINDOWS_CHROME_DRIVER=BASE_PATH+ r'\driver\chromedriver.exe'

    #extract
    WINDOWS_EXTRACT=BASE_PATH+ r'\config\extract.yaml'

    # config
    WINDOWS_CONFIG = BASE_PATH + r'\config\config.yaml'

    if platform.system() == 'Linux':
        pass

    elif platform.system() == 'Windows':

        LOG_PATH = WINDOWS_LOG
        REPORT_DIR = WINDOWS_REPORT_DIR
        EXTRACT_PATH=WINDOWS_EXTRACT
        WINDOWS_CONFIG=WINDOWS_CONFIG


def get_config():
    return Config


if __name__ == '__main__':
    print(os.path.split(os.path.realpath(__file__))[0])
