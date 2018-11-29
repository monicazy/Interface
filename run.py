# -*- coding: utf-8 -*-
# @Time  : 2018/11/13 14:49
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : run.py.py
import unittest
import HTMLTestRunnerNew
from tools.test_case import TestApi
from tools.project_path import test_report_path
from tools.send_email import SendEmail

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestApi))

with open(test_report_path, "wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title="11/10测试报告", description="项目实战", tester="Monica")
    runner.run(suite)

# 生成测试报告后发送给指定收件人
# SendEmail().send_email("3097944154@qq.com", test_report_path)
