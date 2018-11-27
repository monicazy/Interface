# -*- coding: utf-8 -*-
# @Time  : 2018/11/8 22:50
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : http_request.py

import requests
from tools.my_log import MyLog


class HttpRequests:
    def http_requests(self, url, data, method, cookie=None,):
        try:
            res = None
            if method == "get":
                res = requests.get(url, data, cookies=cookie)
            elif method == "post":
                res = requests.post(url, data, cookies=cookie)
            elif method == "put":
                res = requests.put(url, data, cookies=cookie,)
            elif method == "delete":
                res = requests.delete(url, cookies=cookie)
            return res
        except Exception as e:
            MyLog().my_log("ERROR", "出错啦！错误为:{}".format(e))


if __name__ == '__main__':
    a = HttpRequests().http_requests("http://47.107.168.87:8080/futureloan/mvc/api/member/bidLoan",
                                     {'memberId': 43876, 'amount': '100', 'loanId': '5890', 'password': '111111'}, "post")
    print(a.json())