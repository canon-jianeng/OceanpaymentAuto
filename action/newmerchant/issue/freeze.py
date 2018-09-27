#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.newmerchant.issue import freeze as Fre
from action.home.new_merchant import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Fre.Query(driver)
        self.driver = driver

    def query_pay_id(self, pay_id):
        Home(self.driver).click_meun("问题管理", "调单处理")
        self.query.input_pay_id(pay_id)
        self.query.click_query()
        self.query.click_row()
        log.info("查询支付ID")

    def accept_refund(self, pay_id):
        self.query_pay_id(pay_id)
        self.query.click_refund_btn()
        time.sleep(0.5)
        self.query.click_confirm()
        log.info("接受退款")
