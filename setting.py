import os

from cacheout import Cache

BASE_URL = "http://182.92.81.159"


#获取跟目录
CUR_DIR = os.path.abspath(__file__)
#print(CUR_DIR)
BASE_DIR = os.path.dirname(CUR_DIR)
#print(BASE_DIR)

cache = Cache()

class UserInfo(object):

    username = "13800000002"
    password = "123456"

class DbConfig(object):

    de_config = {"host":"182.92.81.159","user":"readuser","password":"iHRM_user_2019","database":"ihrm"}