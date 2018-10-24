#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.merchant import mer_info as Tra
from pageobj.home.admin_system import Common
from action.home.admin_system import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Tra.Query(driver)
        self.assign = Tra.Assign(driver)
        self.common = Common(driver)
        self.driver = driver

    def get_account(self):
        log.info("获取账户号")
        Home(self.driver).merchant_info()
        time.sleep(0.5)
        self.common.click_query()
        return self.common.get_table_val("1", "账户")

    def query_account(self, account):
        Home(self.driver).merchant_info()
        time.sleep(0.5)
        self.query.input_mer_no(account)
        self.common.click_query()
        res = self.common.get_table_val("1", "状态")
        if res == "正常":
            return "1"
        elif res == "未激活":
            return "0"
        log.info("获取账户状态{}".format(res))
        return ""

    def assign_roles(self, account):
        log.info("分配角色权限")
        Home(self.driver).merchant_info()
        time.sleep(0.5)
        self.query.input_mer_no(account)
        self.common.click_query()
        self.common.click_mids()
        self.query.click_assign()
        self.assign.click_all()
        self.common.click_submit()

    def active_account(self, account):
        log.info("激活账户")
        Home(self.driver).merchant_info()
        time.sleep(0.5)
        self.query.input_mer_no(account)
        self.common.click_query()
        self.common.click_mids()
        self.query.click_active()
        self.common.click_confirm()
