#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import os
import sys
import unittest
from common.HTMLTestRunner import HTMLTestRunner
from common.logger import Log

# 当前脚本所在文件真实路径
CUR_PATH = os.path.dirname(os.path.realpath(__file__))

# 日志
log = Log()


def add_case(case_name="testcase", rule="test*.py"):
    """
    第一步：加载所有的测试用例
    :meth case_name: 测试用例文件夹名称 type: str
    :meth rule: 匹配规则 type: str
    :return:
    """
    # 用例文件夹路径
    case_path = os.path.join(CUR_PATH, case_name)
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):
        os.mkdir(case_path)
    log.info("test case path: %s" % case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover


def run_case(all_case, report_name="report"):
    """
    第二步：执行所有的用例, 并把结果写入 HTML 测试报告
    :meth all_case: 所有测试用例 type: str
    :meth report_name: 测试报告文件夹名称 type: str
    :return:
    """
    # now = time.strftime("_%Y-%m-%d %H-%M-%S")
    now = ""
    # 测试报告文件夹
    report_dir = os.path.join(CUR_PATH, report_name)
    # 如果不存在这个report文件夹，就自动创建
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)
    report_abspath = os.path.join(report_dir, "TestResult" + now + ".html")
    log.info("report path: %s" % report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner(stream=fp,
                            title='自动化测试报告,测试结果如下：',
                            description='用例执行情况：')
    # 调用 add_case 函数返回值
    log.info("----- 开始执行测试用例 -----")
    runner.run(all_case)
    log.info("----- 结束执行测试用例 -----")
    fp.close()


def main():
    case_dir = "testcase/newmerchant"
    # 测试项目
    # program = sys.argv[1]
    # if program == "gateway":
    #     case_dir = "testcase/gateway/pay"
    # elif program == "autocheck":
    #     case_dir = "testcase/gateway/check"
    # elif program == "newmerchant":
    #     case_dir = "testcase/newmerchant"
    # 1、加载用例
    load_case = add_case(case_dir)
    # 2、执行用例
    run_case(load_case)


if __name__ == "__main__":
    main()
