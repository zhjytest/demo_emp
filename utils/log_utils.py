
import logging.handlers
from setting import BASE_DIR

#实现日志方法
def log_config():

    #创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    #创建控制器输出器
    sh = logging.StreamHandler()
    #创建文件输出器
    log_file = BASE_DIR +"/logs/ihrm.log"
    th = logging.handlers.TimedRotatingFileHandler(log_file,interval=1,when="midnight",backupCount=7,encoding="utf-8")
    #创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    fomrater = logging.Formatter(fmt)

    #把格式化器加入到输出器
    sh.setFormatter(fomrater)
    th.setFormatter(fomrater)

    #把输出器加入到日志器
    logger.addHandler(sh)
    logger.addHandler(th)