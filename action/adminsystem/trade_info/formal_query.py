#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from pageobj.adminsystem.trade_info import formal_query as Tra
from pageobj.home.admin_system import Common
from action.home.admin_system import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Tra.Query(driver)
        self.common = Common(driver)
        self.driver = driver

    def query_pay_id(self, pay_id):
        Home(self.driver).formal_query()
        self.query.input_pay_id(pay_id)
        self.common.click_query()
        log.info("查询支付ID")

    def get_trade_status(self, val):
        # 获取交易状态
        ele_val = self.common.get_table_val(2, val)
        return self.driver.get_attrval((5, "xpath", ele_val["状态栏"]+"/img[1]"), "title")
