#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from pageobj.newmerchant.refund import refund_apply as Tra
from action.home.new_merchant import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Tra.Query(driver)
        self.driver = driver

    def apply_refund(self, order_num, pay_id, pay_amouont, refund_amount):
        Home(self.driver).click_meun("退款管理", "退款申请")
        self.query.input_order_num(order_num)
        self.query.input_pay_id(pay_id)
        num = int(refund_amount)
        if int(pay_amouont) > num > 0:
            self.query.click_part()
            self.query.input_amount(num)
        self.query.select_reason("客人重复下单")
        self.query.input_refund_des()
        self.query.input_refund_info()
        self.query.click_submit()
        log.info("申请退款")
