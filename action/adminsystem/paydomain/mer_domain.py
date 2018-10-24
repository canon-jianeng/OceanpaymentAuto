#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.paydomain import mer_domain as Tra
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

    def query_domain(self, terminal):
        log.info("查询支付域名")
        Home(self.driver).mer_domain()
        time.sleep(0.5)
        self.query.input_terminal(terminal)
        self.common.click_query()
        time.sleep(0.5)
        res = self.query.get_res_null()
        # 判断是否存在域名绑定的终端号
        if res == "没有找到相关记录，请重新输入条件进行查询 .":
            return res
        return ""

    def create_domain(self, account, terminal, domain_name):
        log.info("新增支付域名")
        Home(self.driver).mer_domain()
        time.sleep(0.5)
        self.query.click_create()
        time.sleep(0.5)
        self.create.input_mer_no(account)
        self.create.select_terminal(terminal)
        self.create.select_md_name(domain_name)
        self.create.select_client_type("PC端")
        self.common.click_submit()
        self.common.confirm_alert()
