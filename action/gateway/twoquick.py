#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from common.conf_utils import Gateway
import pageobj.gateway.submit_page as Sub
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.gate = Gateway()
        self.driver = driver

    def put_create(self, test_data=None):
        """
        quick 2方支付, 创建订单
        :meth test_data: 测试数据 type: dict
        :meth quickid: quickpay_id type: str
        :return:
        """
        if test_data is None:
            test_data = {}
        test_pay = Sub.SubmitPage(self.driver)
        log.info("----- 页面标题: %s -----" % self.driver.title)
        addr = self.gate.read_val("gateway", "proj_domain") + self.gate.read_val("addr", "twocre")
        test_data.update({"提交地址": addr, "接口类型": "create", "quickpay_id": ""})
        for item in test_data:
            tag_name = test_pay.update_info(item, test_data[item])
            if tag_name is not None:
                if tag_name.lower() == "select":
                    log.info("选择{}".format(item))
                elif tag_name.lower() == "input":
                    log.info("输入{}".format(item))
        log.info("点击 make payment")
        test_pay.click_submit("make payemnt")

    def put_pay(self, test_data, quick_id):
        """
        quick 2方支付, 支付订单
        :meth test_data: 测试数据 type: dict
        :meth quickid: quickpay_id type: str
        :return:
        """
        test_pay = Sub.SubmitPage(self.driver)
        log.info("----- 页面标题: %s -----" % self.driver.title)
        addr = self.gate.read_val("gateway", "proj_domain") + self.gate.read_val("addr", "twopay")
        test_data.update({"提交地址": addr, "接口类型": "pay", "quickpay_id": quick_id})
        for item in test_data:
            tag_name = test_pay.update_info(item, test_data[item])
            if tag_name is not None:
                if tag_name.lower() == "select":
                    log.info("选择{}".format(item))
                elif tag_name.lower() == "input":
                    log.info("输入{}".format(item))
        log.info("点击 make payment")
        test_pay.click_submit("make payemnt")
