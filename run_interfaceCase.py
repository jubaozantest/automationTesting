import unittest
import os,time
from lib.HTMLTestRunner import HTMLTestRunner
from util.default_path import get_config
config = get_config()
now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
report_path = config.REPORT_DIR+r'\{0}-interface-report.html'.format(now)
def creatsuite():
    '''添加测试集'''
    testunit = unittest.TestSuite()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.join(dir_path, "testcasesInterface")
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="*.py",
                                                   top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
    return testunit


if __name__ == "__main__":
    suite = creatsuite()
    f = open(report_path,'wb')
    runner=HTMLTestRunner(stream=f,title='聚宝赞接口自动化测试报告',description='描述信息')
    runner.run(suite)
