# -*- coding: utf-8 -*-
# @Time  : 2018/11/9 11:09
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : test_case.py

from tools.http_request import HttpRequests
from tools.readexcel import ReadExcel
from tools.get_data import GetData
from tools.do_regx import DoRegx
from tools.my_log import MyLog
from ddt import ddt, data
from tools.do_mysql import DoMysql
import unittest

# 获取数据相关信息
test_data = ReadExcel().read_excel()
Actual = ""


@ddt
class TestApi(unittest.TestCase):
    def setUp(self):
        MyLog().my_log("INFO", "————————《开始测试》————————")

    @data(*test_data)
    def test_api(self, item):
        global Actual
        MyLog().my_log("INFO", "————————现在执行的用例是：{0}————————".format(item["title"]))
        MyLog().my_log("INFO", "*********此条用例不需要数据库校验:{}*********".format(item["title"]))
        MyLog().my_log("INFO", "————————开始http 接口请求————————")
        MyLog().my_log("INFO", "请求url为：{}".format(item["url"]))
        MyLog().my_log("INFO", "请求参数为：{}".format(item["data"]))
        res = HttpRequests().http_requests(item["url"], eval(item["data"]), item["method"],
                                           getattr(GetData, "Cookie"))
        MyLog().my_log("INFO", "请求结果为：{}".format(res.json()))
        MyLog().my_log("INFO", "————————完成http 接口请求————————")
        if res.cookies:
            setattr(GetData, "Cookie", res.cookies)
        try:
            self.assertEqual(item["ExpectedResult"], res.json()["status"])
            Actual = "Pass"
        except AssertionError as e:
            MyLog().my_log("ERROR", "*****************出错啦！错误为:{}*********".format(e))
            Actual = "Fail"
            raise e
        finally:
            res_code_massage = res.json()
            if "data" in res_code_massage:
                res_code_massage.pop("data")
            ReadExcel().write_back(item["sheet_name"], item["id"] + 1, 9, str(res_code_massage))
            ReadExcel().write_back(item["sheet_name"], item["id"] + 1, 10, Actual)

    def tearDown(self):
        MyLog().my_log("INFO", "————————测试执行结束————————")


if __name__ == '__main__':
    unittest.main()
