import yaml
from util.default_path import get_config

extract_path = get_config().EXTRACT_PATH  #config文件夹中config.yaml路径
config_path = get_config().WINDOWS_CONFIG #config文件夹中extract.yaml路径


class Config:
    def __init__(self):
        '''
        __file__：当前文件路径
        os.path.dirname(file): 某个文件所在的目录路径
        os.path.join(a, b, c,....): 路径构造 a/b/c
        os.path.abspath(path): 将path从相对路径转成绝对路径
        os.pardir: Linux下相当于"../"
        '''
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
        # config_path = os.path.join(dir_path, 'config', 'config.yaml')
        # ,Loader=yaml.FullLoader
        with open(config_path, 'r') as ymlfile:
            self.cfg = yaml.load(ymlfile)

    @property
    def server(self):
        '''
        :return: config.yaml中的serve
        '''
        return self.cfg['server']

    @property
    def browser_name(self):
        '''
        :return: config.yaml中的browser_name
        '''
        return self.cfg['browser']['name']

    @property
    def browser_mode(self):
        '''
        :return: config.yaml中的browser_mode
        '''
        return self.cfg['browser']['mode']

    @property
    def variables_userhost(self):
        return self.cfg['variables']['userhost']

    @property
    def variables_shophost(self):
        return self.cfg['variables']['shophost']

    @property
    def variables_siteId(self):
        return self.cfg['variables']['siteId']

    def variables(self, name):
        return self.cfg['variables'][name]


class ConfigExtract:
    '''
    读取 提取变量yaml文件
    '''
    def __init__(self):
        with open(extract_path, 'r') as ymlfile:
            self.cfg = yaml.load(ymlfile)

    def extract(self, variable):
        return self.cfg[variable]


read_basic_config = Config()
read_extract_config = ConfigExtract()
