#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.risk_control import mer_web_white as Tra
from pageobj.home.admin_system import Common
from action.home.admin_system import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Tra.Query(driver)
        self.create = Tra.Create(driver)
        self.common = Common(driver)
        self.driver = driver

    def query_web_white(self, terminal):
        log.info("查询网址白名单")
        Home(self.driver).merweb_white()
        time.sleep(0.5)
        self.query.input_terminal(terminal)
        self.common.click_query()
        time.sleep(0.5)
        # 判断是否存在网址白名单的终端号
        res = self.query.get_res_null()
        if res == "没有找到相关记录，请重新输入条件进行查询 .":
            return res
        else:
            res = self.common.get_table_val("1", "状态")
            if res == "已审核":
                return "1"
            elif res == "待处理":
                return "0"
        return ""

    def create_web_white(self, account, terminal):
        log.info("新增网址白名单")
        Home(self.driver).merweb_white()
        time.sleep(0.5)
        self.query.click_create()
        time.sleep(0.5)
        self.create.input_mer_no(account)
        self.create.click_terminal(terminal)
        self.create.input_websit("www.baidu.com")
        self.common.click_submit()
        self.common.confirm_alert()

    def review_web_white(self, terminal):
        log.info("审核网址白名单")
        Home(self.driver).merweb_white()
        time.sleep(0.5)
        self.query.input_terminal(terminal)
        self.common.click_query()
        time.sleep(0.5)
        self.common.click_mids()
        self.query.click_review()
        # 判断是否出现警告框
        is_alert = self.common.confirm_alert()
        if not is_alert:
            self.common.click_submit()

    def verify_web_white(self, terminal):
        log.info("复核网址白名单")
        Home(self.driver).merweb_white()
        time.sleep(0.5)
        self.query.input_terminal(terminal)
        self.common.click_query()
        time.sleep(0.5)
        self.common.click_mids()
        self.query.click_verify()
        # 判断是否出现警告框
        is_alert = self.common.confirm_alert()
        if not is_alert:
            self.common.click_submit()
