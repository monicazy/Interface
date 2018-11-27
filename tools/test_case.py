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
        MyLog().my_log("INFO", "————————开始测试————————")

    @data(*test_data)
    def test_api(self, item):
        global Actual
        MyLog().my_log("INFO", "————————现在执行的用例是：{0}————————".format(item["title"]))

        # 如果找到&{loanId}
        if item["data"].find("&{loanId}")!=-1:
            # 如果loanId还没有取到生成的值，就查询数据库去获取值用来替换用例中的参数，同时保存这个值到工具类中
            if getattr(GetData, "loanId") == None:
                loanId = DoMysql().do_mysql("SELECT max(Id) FROM loan WHERE MemberID={0}".format(getattr(GetData,"loan_member_id")))[0][0]
                item["data"] = item["data"].replace("&{loanId}", str(loanId))
                setattr(GetData, "loan_Id", loanId)
                MyLog().my_log("INFO", "*****************为None时data替换结果为：{}".format(eval(item["data"])))
            else:  # 如果已经有loanId就直接替换不用查询数据库了
                item["data"] = DoRegx().do_regx(item["data"])
                # 日志打印
                MyLog().my_log("INFO", "***************反射获取到loan_id的结果为：{}".format(getattr(GetData, "loanId")))
                MyLog().my_log("INFO", "***************反射后获取到data结果为：{}".format(eval(item["data"])))

        # 如果存在check_sql，那么就做数据库校验
        if eval(item["check_sql"]) != None:
            MyLog().my_log("INFO", "*********此条用例需要数据库校验:{}.*********".format(item["title"]))
            query_sql=eval(item["check_sql"])["sql"]
            Before_Amount=DoMysql().do_mysql(query_sql)[0][0]
            MyLog().my_log("INFO", "*********用例:{}请求之前的余额为：{}.*********".format(item["title"],Before_Amount))
            MyLog().my_log("INFO", "————————开始http 接口请求————————")
            MyLog().my_log("INFO", "请求参数为：{}".format(item["data"]))
            res = HttpRequests().http_requests(item["url"], eval(item["data"]), item["method"],
                                               getattr(GetData, "Cookie"))
            MyLog().my_log("INFO", "请求结果为：{}".format(res.json()))
            MyLog().my_log("INFO", "————————完成http 接口请求————————")
            After_Amount = DoMysql().do_mysql(query_sql)[0][0]
            MyLog().my_log("INFO", "*********用例:{}请求之后的余额为：{}.*********".format(item["title"], After_Amount))

            # 检查结果
            if float(eval(item["data"])["amount"]) == float(abs(After_Amount-Before_Amount)):
                MyLog().my_log("INFO", "*********数据库校验余额通过*********")
                check_sql_result= "校验余额通过"
            else:
                MyLog().my_log("INFO", "*********数据库校验余额不通过*********")
                check_sql_result = "校验余额不通过"
            # 检查结果写回excel
            ReadExcel().write_back(item["sheet_name"], item["id"] + 1, 11, check_sql_result)
        else:
            MyLog().my_log("INFO", "*********此条用例不需要数据库校验:{}*********".format(item["title"]))
            MyLog().my_log("INFO", "————————开始http 接口请求————————")
            MyLog().my_log("INFO", "请求参数为：{}".format(item["data"]))
            res = HttpRequests().http_requests(item["url"], eval(item["data"]), item["method"],
                                               getattr(GetData, "Cookie"))
            MyLog().my_log("INFO", "请求结果为：{}".format(res.json()))
            MyLog().my_log("INFO", "————————完成http 接口请求————————")


        if res.cookies:
            setattr(GetData, "Cookie", res.cookies)
        try:
            self.assertEqual(str(item["ExpectedResult"]), res.json()["code"])
            Actual = "Pass"
        except AssertionError as e:
            MyLog().my_log("ERROR", "*****************出错啦！错误为:{}*********".format(e))
            Actual = "Fail"
            raise e
        finally:
            ReadExcel().write_back(item["sheet_name"], item["id"] + 1,9, str(res.json()))
            ReadExcel().write_back(item["sheet_name"], item["id"] + 1,10, Actual)

    def tearDown(self):
        MyLog().my_log("INFO", "————————测试执行结束————————")


if __name__ == '__main__':
    unittest.main()
