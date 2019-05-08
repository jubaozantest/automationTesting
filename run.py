import unittest
import os,sys,getopt,time
from lib.HTMLTestRunner_hjh import HTMLTestRunner
from util.default_path import get_config
config = get_config()
now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
#report_path = config.REPORT_DIR+r'\test{0}.html'.format(int(time.time())) #报告名称加上时间戳
report_path = config.REPORT_DIR+r'\{0}-report.html'.format(now)           #报告名称加上当前时间
def creatsuite():
    '''添加测试集'''
    testunit = unittest.TestSuite()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.join(dir_path, "testcases")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="testcases*.py",
                                                   top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit

def getopts():
    try:
        options,args = getopt.getopt(sys.argv[1:],"r:p",["runner=","project="])
        for o,v in options:
            if o in ("-r","--runner"):
                # Feie.runner = int(v)
                print(v)
            if o in ("-p","--project"):
                # Feie.project = int(v)
                print(v)
    except getopt.GetoptError as err:
      print(str(err))
      sys.exit(1)

if __name__ == "__main__":
    getopts()
    suite = creatsuite()

    #unittest.TextTestRunner(verbosity=2).run(suite)
    #f = open(r'C:\Users\MIME\Desktop\test.html', 'wb')
    f = open(report_path,'wb')
    runner=HTMLTestRunner(stream=f,title='自动化测试报告',description='描述信息')
    runner.run(suite)
