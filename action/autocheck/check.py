#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import pageobj.gateway.submit_page as Sub
from common.conf_utils import AutoCheck
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.check = AutoCheck()
        self.driver = driver

    def put_check(self, test_data, num):
        """
        提交对账
        :meth test_data: 测试数据 type: dict
        :meth num: 网站订单号 type: str
        :return:
        """
        if test_data is None:
            test_data = {}
        test_pay = Sub.SubmitPage(self.driver)
        log.info("----- 页面标题: %s -----" % self.driver.title)
        addr = self.check.read_val("autocheck", "proj_domain") + self.check.read_val("addr", "check")
        test_data.update({"提交地址": addr, "网站订单号": num})
        for item in test_data:
            tag_name = test_pay.update_info(item, test_data[item])
            if tag_name is not None:
                if tag_name.lower() == "select":
                    log.info("选择{}".format(item))
                elif tag_name.lower() == "input":
                    log.info("输入{}".format(item))
        log.info("点击检索交易结果")
        test_pay.click_submit("检索交易结果")

    def put_track(self, test_data, pay_id):
        """
        提交物流信息上传
        :meth test_data: 提交地址选项值 type: dict
        :meth pay_id: 支付ID type: str
        :return:
        """
        if test_data is None:
            test_data = {}
        test_pay = Sub.SubmitPage(self.driver)
        log.info("----- 页面标题: %s -----" % self.driver.title)
        addr = self.check.read_val("autocheck", "proj_domain") + self.check.read_val("addr", "track")
        test_data.update({"提交地址": addr, "支付ID": pay_id})
        for item in test_data:
            tag_name = test_pay.update_info(item, test_data[item])
            if tag_name is not None:
                if tag_name.lower() == "select":
                    log.info("选择{}".format(item))
                elif tag_name.lower() == "input":
                    log.info("输入{}".format(item))
        log.info("点击物流信息上传")
        test_pay.click_submit("物流信息上传")

    def apply_refund(self, test_data, pay_id):
        """
        申请退款
        :meth test_data: 测试数据 type: dict
        :meth pay_id: 支付ID type: str
        :return:
        """
        if test_data is None:
            test_data = {}
        test_pay = Sub.SubmitPage(self.driver)
        log.info("----- 页面标题: %s -----" % self.driver.title)
        addr = self.check.read_val("autocheck", "proj_domain") + self.check.read_val("addr", "apply_ref")
        test_data.update({"提交地址": addr, "支付ID": pay_id})
        for item in test_data:
            tag_name = test_pay.update_info(item, test_data[item])
            if tag_name is not None:
                if tag_name.lower() == "select":
                    log.info("选择{}".format(item))
                elif tag_name.lower() == "input":
                    log.info("输入{}".format(item))
        log.info("点击退款申请")
        test_pay.click_submit("退款申请")

    def query_refund(self, test_data, ref_id):
        """
        查询退款信息
        :meth test_data: 测试数据 type: dict
        :meth ref_id: 退款ID type: str
        :return:
        """
        if test_data is None:
            test_data = {}
        test_pay = Sub.SubmitPage(self.driver)
        log.info("----- 页面标题: %s -----" % self.driver.title)
        addr = self.check.read_val("autocheck", "proj_domain") + self.check.read_val("addr", "query_ref")
        test_data.update({"提交地址": addr, "退款ID": ref_id})
        for item in test_data:
            tag_name = test_pay.update_info(item, test_data[item])
            if tag_name is not None:
                if tag_name.lower() == "select":
                    log.info("选择{}".format(item))
                elif tag_name.lower() == "input":
                    log.info("输入{}".format(item))
        log.info("点击退款查询")
        test_pay.click_submit("退款查询")
