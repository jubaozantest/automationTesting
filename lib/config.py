# -*- coding=utf-8
import os
import yaml

class  Config:
    def __init__(self):
        '''
        __file__：当前文件路径
        os.path.dirname(file): 某个文件所在的目录路径
        os.path.join(a, b, c,....): 路径构造 a/b/c
        os.path.abspath(path): 将path从相对路径转成绝对路径
        os.pardir: Linux下相当于"../"
        '''
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
        config_path = os.path.join(dir_path, 'config', 'config.yaml')
        with open(config_path, 'r') as ymlfile:
            self.cfg = yaml.load(ymlfile)
    @property
    def server(self):
        return self.cfg['server']


    @property
    def browser_name(self):
        return self.cfg['browser']['name']

    @property
    def browser_mode(self):
        return self.cfg['browser']['mode']

test_config = Config()
