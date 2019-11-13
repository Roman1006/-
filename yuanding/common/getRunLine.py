#!/usr/bin/python3
# coding=utf-8
import sys


def get_run_line():
    """获取当前代码执行的行号
    :return: 调用者的当前行号
    """
    try:
        raise Exception
    except:
        f = sys.exc_info()[2].tb_frame.f_back
    line = f.f_code.co_name, f.f_lineno
    return line[1]
