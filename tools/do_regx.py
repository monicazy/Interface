# -*- coding: utf-8 -*-
# @Time  : 2018/11/25 21:19
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : do_regx.py
import re
from tools.get_data import GetData

class DoRegx:
    @staticmethod
    def do_regx(str_name):
        while re.search("\$\{(.*?)\}", str_name):
            key =re.search("\$\{(.*?)\}", str_name).group(0)
            vaule = re.search("\$\{(.*?)\}", str_name).group(1)
            str_name = str_name.replace(key, str(getattr(GetData, vaule)))  # 替换变量值
        return str_name

if __name__ == '__main__':
    s = '{"mobilephone":"${normal_tel}","amount":"10000"}'
    s1 = '{"mobilephone":"111","amount":"10000"}'
    print(DoRegx().do_regx(s))