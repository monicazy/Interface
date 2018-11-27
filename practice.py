# -*- coding: utf-8 -*-
# @Time  : 2018/11/9 10:33
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : practice.py

# 执行代码的入口
# data_1 = dict(register=[0], login=[0, 1, 2], recharge=[0, 1, 2, 3])
# print(list(data))
# print(list(data.keys()))
# print(list(data.values()))
# print(list(data.items()))
# print(list(zip(*(data.items()))))

# data = str({"a_register": "${tel}", "b_login": [0, 1, 2], "c_recharge": [0, 1]})
# a = [key for key in sorted(data.keys())]
# b = [value for value in data.values()]
# print(a)
# print(b)
# tel=123
# if data.find("${tel}")!=-1:
#     data=data.replace("${tel}",str(tel))
# print(data)
# import pymysql
# import mysql.connector
# mydb = pymysql.connect(host='47.107.168.87',port=3306,user='python',password='python666',db="test")
# cursor = mydb.cursor()
# cursor.execute("SELECT * FROM student")
# results = cursor.fetchall()
# print(results)
# mydb.close()
# # 连接数据库
# connection = mysql.connector.connect(host='47.107.168.87',port=3306,user='python',password='python666',db="test")
# # 获取游标
# cursor = connection.cursor()
# # 查询数据
# re = cursor.execute('SELECT Sname FROM student')
# # 返回查询结果集的所有行
# results = cursor.fetchall()
# print(results)
# connection.close()

# import pandas as pd
# from tools import project_path
# df=pd.read_excel(project_path.test_case_path, sheet_name="init")
# tel = df.iloc[0,0]
# print(tel)

import re
from tools.get_data import GetData
# s = "llal,alllafl" # 目标字符串
# res=re.match("(llal)",s) # 全匹配，头部匹配
# print(res.group()) # group()==group(0) 拿到匹配的全字符，按你正则里的要求匹配分组
# d="dddg,gdgg,hhh"
# ress=re.findall("(d)(g)",d) # 列表 在字符串里面找 匹配的内容 存在列表里面
# # 如果有分组 就是以元组的形式表现出来 列表嵌套元组
# print(ress)
s ='{"mobilephone":"${normal_tel}","amount":"10000"}'
res=re.search("\$\{(.*?)\}",s)
print(res)
key=res.group()
vaule=res.group(1)
new_s = s.replace(key,str(getattr(GetData,vaule)))# 替换变量值
print(new_s)
