#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.terminal import ter_query as Tra
from pageobj.home.admin_system import Common
from action.home.admin_system import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Tra.Query(driver)
        self.create = Tra.Create(driver)
        self.modify = Tra.Modify(driver)
        self.common = Common(driver)
        self.driver = driver

    def get_terminal(self, account):
        log.info("获取终端号")
        Home(self.driver).terminal_query()
        time.sleep(0.5)
        self.query.input_mer_no(account)
        self.common.click_query()
        return self.common.get_table_val("1", "终端号")

    def query_terminal(self, terminal):
        Home(self.driver).terminal_query()
        time.sleep(0.5)
        self.query.input_terminal(terminal)
        self.common.click_query()
        time.sleep(0.5)
        log.info("查询终端号是否存在")
        # 判断终端号是否存在
        return self.query.get_res_null()

    def query_list(self, terminal, name):
        Home(self.driver).terminal_query()
        time.sleep(0.5)
        self.query.input_terminal(terminal)
        self.common.click_query()
        time.sleep(0.5)
        res = self.common.get_table_val("1", name)
        log.info("获取{}: {}".format(name, res))
        return res

    def modify_terminal(self, terminal, inf_type):
        log.info("修改终端号")
        Home(self.driver).terminal_query()
        time.sleep(0.5)
        self.query.input_terminal(terminal)
        self.common.click_query()
        time.sleep(0.5)
        self.common.click_mids()
        self.query.click_modify()
        time.sleep(0.5)
        self.modify.input_secure_code("12345678")
        self.modify.select_inf_type(inf_type)
        self.modify.select_bus_type("商户行业")
        self.modify.click_ip_no()
        self.modify.input_pay_times()
        self.modify.select_model("推送和正常返回")
        self.common.click_submit()
        self.common.confirm_alert()

    def create_terminal(self, account, inf_type):
        log.info("新增终端号")
        Home(self.driver).terminal_query()
        time.sleep(0.5)
        self.query.click_create()
        time.sleep(0.5)
        self.create.input_mer_no(account)
        self.create.input_secure_code("12345678")
        self.create.select_inf_type(inf_type)
        self.create.select_bus_type("商户行业")
        self.create.click_ip_no()
        self.create.input_pay_times()
        self.create.select_model("推送和正常返回")
        self.common.click_submit()
        self.common.confirm_alert()

    def active_terminal(self, terminal):
        log.info("激活终端号")
        Home(self.driver).terminal_query()
        time.sleep(0.5)
        self.query.input_terminal(terminal)
        self.common.click_query()
        time.sleep(0.5)
        self.common.click_mids()
        self.query.click_active()
        self.common.confirm_alert()

    def start_terminal(self, terminal):
        log.info("启用终端号")
        Home(self.driver).terminal_query()
        time.sleep(0.5)
        self.query.input_terminal(terminal)
        self.common.click_query()
        time.sleep(0.5)
        self.common.click_mids()
        self.query.click_start()
        time.sleep(0.5)
        self.common.confirm_alert()
