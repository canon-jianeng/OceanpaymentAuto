#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.risk_control import risk_monitor as Tra
from pageobj.home.admin_system import Common
from action.home.admin_system import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Tra.Query(driver)
        self.create_obj = Tra.Create(driver)
        self.common = Common(driver)
        self.driver = driver

    def query_pay_id(self, pay_id):
        log.info("查询支付ID:{}".format(pay_id))
        Home(self.driver).risk_monitor()
        self.query.input_pay_id(pay_id)
        self.common.click_query()

    def get_counterfeit(self, val):
        # 获取伪冒状态
        return self.query.get_table_val(1, val)

    def create(self, pay_id, reason):
        log.info("新增伪冒")
        time.sleep(0.5)
        self.common.click_mids()
        self.query.click_counterfeit()
        time.sleep(0.5)
        self.create_obj.input_pay_id(pay_id)
        self.create_obj.input_uo_time()
        self.create_obj.select_reason(reason)
        self.common.click_submit()
