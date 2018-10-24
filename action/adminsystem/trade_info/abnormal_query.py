#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.trade_info import abnormal_query as Tra
from pageobj.home.admin_system import Common
from action.home.admin_system import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Tra.Query(driver)
        self.review_obj = Tra.Review(driver)
        self.verify_obj = Tra.Verify(driver)
        self.common = Common(driver)
        self.driver = driver

    def query_abn_type(self, pay_id, abn_type):
        log.info("查询支付ID和异常类型:{}".format(abn_type))
        Home(self.driver).abn_query()
        self.query.input_pay_id(pay_id)
        self.query.select_abn_type(abn_type)
        self.common.click_query()

    def get_query_result(self, val):
        # 获取查询结果
        return self.common.get_table_val(1, val)

    def review(self):
        log.info("异常交易查询 - 审核")
        time.sleep(0.5)
        self.common.click_mids()
        self.query.click_review()
        time.sleep(0.5)
        self.review_obj.select_status("通过")
        self.common.click_submit()

    def verify(self):
        log.info("异常交易查询 - 复核")
        time.sleep(0.5)
        self.common.click_mids()
        self.query.click_verify()
        time.sleep(0.5)
        self.verify_obj.select_status("通过")
        self.common.click_submit()
