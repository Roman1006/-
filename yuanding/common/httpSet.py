import json
import requests
from common.myLog import MyLog
from  requests.cookies import RequestsCookieJar
import re

false = False
true = True


class HttpMethod:
    def __init__(self):
        self.log = MyLog()
        self.cookies = requests.cookies.RequestsCookieJar()

    def go(self,url,method,data):
        response = requests.request(method,url
                                    ,data=data
                                    ,cookies = self.cookies)#传递cookie
        self.cookies.update(response.cookies)#保存cookie
        return response.cookies

    def get_method(self, url, data=None, headers=None):
        try:
            res = requests.get(url=url, params=data, headers=headers)
            status_code = res.status_code
            header_token = res.headers
            res_json = res.json()
            return status_code,header_token, res_json  # 返回响应码，响应内容
        except Exception as e:
            self.log.error("Error:%s" % e)

    def post_method(self,url, files=None,data=None,headers=None):
        try:
            if files:
                res = requests.post(url=url, files=files, data=data, headers=headers)
            else:
                res = requests.post(url=url, data=json.dumps(data),headers=headers)#json.dumps(data)
            status_code = res.status_code
            res_json = res.json()
            return status_code, res_json  # 返回响应码，响应内容
        except Exception as e:
            self.log.error("Error:%s" % e)

    def put_method(self, url, data=None, headers=None):
        try:
            res = requests.put(url=url, data=json.dumps(data), headers=headers)
            status_code = res.status_code
            res_json = res.json()
            return status_code, res_json  # 返回响应码，响应内容
        except Exception as e:
            self.log.error("Error:%s" % e)

    def delete_method(self, url, data=None, headers=None):
        try:
            res = requests.delete(url=url, data=json.dumps(data), headers=headers)
            status_code = res.status_code
            res_json = res.json()
            return status_code, res_json  # 返回响应码，响应内容
        except Exception as e:
            self.log.error("Error:%s" % e)

    def http_method(self, method, url, files=None, data=None, headers=None):
        """判断请求方法
        :param method: 请求方法
        :param url: 接口路径
        :param data: 请求数据
        :param headers: 请求头
        :return:
        """
        if method == 'get':
            status_code,header_token, res_json = self.get_method(url, data, headers)
        elif method == 'post':
            # status_code, res_json = self.post_method(url, files, data, headers)
            res_json = requests.post (url=url, data=data,headers=headers)
            # print(res_json.text)
            status_code = res_json.status_code
            header_token = res_json.headers
            res_json = res_json.json()
        elif method == 'put':
            status_code, res_json = self.put_method(url, data, headers)
        else:
            status_code, res_json = self.delete_method(url, data, headers)
        return status_code,header_token, json.dumps(res_json, ensure_ascii=False, sort_keys=False, indent=2)  # 对json数据进行格式化输出

