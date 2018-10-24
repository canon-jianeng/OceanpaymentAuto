#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.agent import agent_mer as Tra
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

    def query_agent(self, account):
        log.info("查询账户绑定代理商")
        Home(self.driver).agent_merchant()
        time.sleep(0.5)
        self.query.input_mer_no(account)
        self.common.click_query()
        time.sleep(0.5)
        res = self.query.get_res_null()
        if res == "没有找到相关记录，请重新输入条件进行查询 .":
            return res
        return ""

    def create_agent(self, account, terminal):
        log.info("创建账户绑定代理商")
        Home(self.driver).agent_merchant()
        time.sleep(0.5)
        self.query.click_create()
        time.sleep(1)
        self.create.input_agent_no("1002")
        self.create.input_mer_no(account)
        self.create.select_terminal(terminal)
        self.common.click_submit()
