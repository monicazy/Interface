# -*- coding: utf-8 -*-
# @Time  : 2018/11/22 17:31
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : do_mysql.py
import mysql.connector
from tools.project_path import case_config_path
from tools.do_config import Readconfig
from tools.readexcel import ReadExcel


class DoMysql:

    def do_mysql(self, query):
        # 从配置文件读取db_config的配置参数
        db_config = eval(Readconfig().read_config(case_config_path, "DB", "db"))
        # 连接数据库
        connection = mysql.connector.connect(**db_config)
        # 获取游标
        cursor = connection.cursor()
        # 查询数据
        cursor.execute(query)
        # 返回查询结果集的所有行
        results = cursor.fetchall()
        # 关闭数据库连接
        connection.close()
        return results


if __name__ == '__main__':
    print(DoMysql().do_mysql('SELECT max(Id) FROM loan WHERE MemberID="24711"')[0][0])
    # print(eval(Readconfig().read_config(case_config_path, "DB", "db")))
