import logging
from util.default_path import get_config
config = get_config()
log_path = config.LOG_PATH

logger=logging.getLogger('test')
#logging.basicConfig() #不用basicConfig 需要手动添加handler
logger.setLevel(logging.DEBUG) #输出所有大于DEBUG级别的log
#设置日志输出格式
fmt = logging.Formatter('[%(filename)-6s]: [%(levelname)-6s] [%(asctime)s]: %(message)s')
#console打印,级别为warning
stream_hdl = logging.StreamHandler()
stream_hdl.setFormatter(fmt)
stream_hdl.setLevel(logging.INFO)
logger.addHandler(stream_hdl)

#输入文件流,级别为debug
file_hdl = logging.FileHandler(log_path)
file_hdl.setFormatter(fmt)
file_hdl.setLevel(logging.DEBUG)
logger.addHandler(file_hdl)


if __name__ == "__main__":

    for i in range(1):
        logger.debug("This is debug information")
        logger.info("This is info information")
        logger.error("This is error information")
