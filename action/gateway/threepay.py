#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import re
import pageobj.gateway.submit_page as Sub
from common.conf_utils import Gateway
from common.logger import Log
from action.gateway import pay as Pa

log = Log()


class Action(object):
    def __init__(self, driver):
        self.gate = Gateway()
        self.driver = driver

    def put_three(self, test_data1=None, test_data2=None, payval=None):
        """
        提交 3方支付
        :meth test_data1: 测试数据, 交易信息 type: dict
        :meth test_data2: 测试数据, 信用卡信息 type: dict
        :meth payval: 支付域名列表 type: list
        :return:
        """
        if test_data1 is None:
            test_data1 = {}
        elif test_data2 is None:
            test_data2 = {}
        test_pay = Sub.SubmitPage(self.driver)
        log.info("----- 页面标题: %s -----" % self.driver.title)
        addr = self.gate.read_val("gateway", "proj_domain") + self.gate.read_val("addr", "thr")
        test_data1.update({"提交地址": addr})
        for item in test_data1:
            tag_name = test_pay.update_info(item, test_data1[item])
            if tag_name is not None:
                if tag_name.lower() == "select":
                    log.info("选择{}: {}".format(item, test_data1[item]))
                elif tag_name.lower() == "input":
                    log.info("输入{}: {}".format(item, test_data1[item]))
        log.info("点击 make payment")
        test_pay.click_submit("make payemnt")
        # 信用卡支付
        domain = re.findall(r"/\w+/\w+\.", self.driver.current_url)[0].replace(".", "")
        for val in payval:
            for domain_conf in val[1].split(","):
                if domain == domain_conf.strip():
                    getattr(Pa.PayAction(self.driver), val[0])(test_data2)
                    break
