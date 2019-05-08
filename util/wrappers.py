
import functools
import time
import traceback
from  logs.log import logger
from flask import jsonify

def timer(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kw):
        who = 'hejianhao'
        logger.info('<==================== {1} Begin call [{0}] ===================='.format(__get_full_class(self), who))
        start_time = time.time()
        try:
            c = func(self, *args, **kw)
        except Exception as err:
            text = '\n'.join(['an error occured ', str(err), traceback.format_exc()])
            logger.error('ATP: 接口发现未知错误 \n {traceback}'.format(traceback=text))

            c = jsonify({"code": "999", "desc": "system error"})
        end_time = time.time()
        d_time = end_time - start_time
        logger.info("==================== End call [{0}], run {1:.3}s ====================>\n"
                    .format(__get_full_class(self), d_time))
        return c

    return wrapper



def __get_full_class(obj):
    return "{0}.{1}".format(obj.__module__, obj.__class__.__name__)


