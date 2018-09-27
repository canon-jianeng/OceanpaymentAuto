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

    def auth(self, test_data, pay_id, order_num):
        """
        预授权
        :param test_data: 测试数据 type: dict
        :param pay_id: 支付ID type: str
        :param order_num: 商户订单 type: str
        """
        if test_data is None:
            test_data = {}
        test_pay = Sub.SubmitPage(self.driver)
        log.info("----- 页面标题: %s -----" % self.driver.title)
        addr = self.gate.read_val("gateway", "proj_domain") + self.gate.read_val("addr", "auth")
        test_data.update({"提交地址": addr, "支付ID": pay_id, "商户订单": order_num})
        for item in test_data:
            tag_name = test_pay.update_info(item, test_data[item])
            if tag_name is not None:
                if tag_name.lower() == "select":
                    log.info("选择{}".format(item))
                elif tag_name.lower() == "input":
                    log.info("输入{}".format(item))
        log.info("点击确定")
        test_pay.click_submit("确定")
