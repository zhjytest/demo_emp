
"""
    功能:实现接口的基类
        功能1：解决所有的url
        功能2：解决的请求方法，post,get,put,delete
        功能3：解决headers
"""

#导包
import requests
import logging
from setting import BASE_URL, UserInfo,cache


class Base(object):

    def __init__(self):
        self.headers = {"Content-Type":"application/json"}

    # 返回接口url
    def get_url(self,url,target=None):
        if target:
            if isinstance(target,int):
                target = str(target)
            return BASE_URL + url +'/' + target
        return BASE_URL + url

    # 实现headers
    def _headers(self):
        data = cache.get('headers')
        if data:
            logging.info("从缓存取的数据：{}".format(data))
            return data
        res = self.__login(UserInfo.username,UserInfo.password)
        logging.info("请求登录接口获取数据:{}".format(res))
        return res


    #实现登录
    def __login(self,mobile,password):
        login_data = {"mobile":mobile,"password":password}
        result = requests.post(self.get_url("/api/sys/login"),json=login_data).json()
        logging.info("login result:{}".format(result))
        str_data = result.get('data')
        if str_data:
            token = "Bearer " + str_data
            self.headers['Authorization'] = token
            cache.set("headers",self.headers)
        return self.headers


    # post请求方法
    def post(self,url,data=None):
        try:
            response = requests.post(url,json=data,headers=self._headers())
            #print("response:{}".format(response))
            assert 200 == response.status_code
            return response.json()
        except Exception as e:
            logging.error("请求post方法异常:{}".format(e))

    # get请求方法
    def get(self,url):
        try:
            response = requests.get(url,headers=self._headers())
            #print("response:{}".format(response))
            assert 200 == response.status_code
            return response.json()
        except Exception as e:
            logging.error("请求get方法异常:{}".format(e))


    # delete请求方法
    def delete(self,url):
        try:
            response = requests.delete(url,headers=self._headers())
            #print("response:{}".format(response))
            assert 200 == response.status_code
            return response.json()
        except Exception as e:
            logging.error("请求delete方法异常:{}".format(e))


if __name__ == '__main__':
    b = Base()
    print(b.post(b.get_url("/api/sys/profile")))
    print(b.post(b.get_url("/api/sys/profile")))