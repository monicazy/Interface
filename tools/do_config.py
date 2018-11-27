# -*- coding: utf-8 -*-
# @Time  : 2018/11/8 23:27
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : do_config.py
import configparser


class Readconfig:
    def read_config(self, file_name, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8")
        return cf.get(section, option)


if __name__ == '__main__':
    # print(Readconfig().read_config('I:\lesson_practice\Interface\\testdata\\case.config', 'DATA', 'file_name'))
    from tools import project_path
    a = Readconfig().read_config(project_path.case_config_path, 'DATA', 'file_name')
    print(a)