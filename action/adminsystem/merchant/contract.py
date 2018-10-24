#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.merchant import contract as Tra
from pageobj.home.admin_system import Common
from action.home.admin_system import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Tra.Query(driver)
        self.create = Tra.Create(driver)
        self.verify = Tra.Verify(driver)
        self.common = Common(driver)
        self.driver = driver

    def query_contract(self, account):
        log.info("查询合同信息")
        Home(self.driver).merchant_contract()
        time.sleep(0.5)
        self.query.input_mer_no(account)
        self.common.click_query()
        time.sleep(0.5)
        # 判断是否审核/复核合同信息
        res = self.common.get_table_val("1", "状态")
        if res == "已审核":
            return "1"
        elif res == "已复核(成功)":
            return "2"
        return ""

    def create_contract(self, account):
        log.info("新增合同信息")
        Home(self.driver).merchant_contract()
        time.sleep(0.5)
        self.query.click_create()
        time.sleep(0.5)
        self.create.input_mer_no(account)
        self.create.select_init_date()
        self.create.select_end_date()
        self.create.click_auto_renew()
        self.create.select_contract_type("a101")
        self.create.select_start_date()
        self.common.click_submit()

    def verify_contract(self, account):
        log.info("复核合同信息")
        Home(self.driver).merchant_contract()
        time.sleep(0.5)
        self.query.input_mer_no(account)
        self.common.click_query()
        self.common.click_mids()
        self.query.click_verify()
        # 判断是否出现警告框
        is_alert = self.common.confirm_alert()
        if not is_alert:
            self.verify.select_status("已复核(成功)")
            self.common.click_submit()
