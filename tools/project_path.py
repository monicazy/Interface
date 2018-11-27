# -*- coding: utf-8 -*-
# @Time  : 2018/11/18 14:24
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : project_path.py
import os

'''专门来读取路径的值'''
# 获取顶级目录的路径
project_path = os.path.split(os.path.dirname(__file__))[0]
# 测试用例的路径
test_case_path = os.path.join(project_path, 'test_data', 'test_data.xlsx')

# 测试报告的路径
test_report_path = os.path.join(project_path, 'test_result', 'html_report', 'test_report.html')

# 配置文件的路径
case_config_path = os.path.join(project_path, 'conf', 'case.config')

# 配置log路径
logs_path = os.path.join(project_path, 'test_result', 'log', 'log.txt')


