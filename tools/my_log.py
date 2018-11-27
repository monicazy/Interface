# -*- coding: utf-8 -*-
# @Time  : 2018/11/18 14:54
# @Author : Monica
# @Email : 498194410@qq.com
# @File  : my_log.py
import logging
from tools import project_path


class MyLog:
    def my_log(self, level, msg):
        # 定义一个日志收集器my_logger
        my_logger = logging.getLogger("Monica")

        # 设定级别
        my_logger.setLevel("DEBUG")

        # 设置日志输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        # 创造一个专属输出渠道  过滤 和排版
        ch = logging.StreamHandler()  # 输出到控制台
        ch.setLevel("DEBUG")  # 设置输出级别  大写
        ch.setFormatter(formatter)

        fh = logging.FileHandler(project_path.logs_path, encoding='UTF-8')  # 输出到制定文件
        fh.setLevel("DEBUG")  # 设置输出级别  大写
        fh.setFormatter(formatter)

        # 两者对接--指定输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # 渠道要记得移除掉 否则 日志输出会重复
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log("DEBGU", msg)

    def info(self, msg):
        self.my_log("INFO", msg)

    def warning(self, msg):
        self.my_log("ERROR", msg)

    def error(self, msg):
        self.my_log("WARNING", msg)

    def critical(self, msg):
        self.my_log("CRITICAL", msg)

# if __name__ == '__main__':
#     MyLog().my_log("INFO","啦啦啦")
