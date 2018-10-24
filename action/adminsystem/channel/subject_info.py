#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.channel import subject_info as Tra
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

    def query_subject(self, bank, subject, settle):
        log.info("查询主体信息")
        Home(self.driver).subject_info()
        time.sleep(0.5)
        self.query.select_bank_name(bank)
        self.query.select_subject(subject)
        self.query.select_settle(settle)
        self.common.click_query()
        time.sleep(0.5)
        res = self.query.get_res_null()
        if res == "没有找到相关记录，请重新输入条件进行查询 .":
            return res
        return ""

    def create_subject(self, data_dict):
        log.info("创建主体信息")
        Home(self.driver).subject_info()
        time.sleep(0.5)
        self.query.click_create()
        time.sleep(0.5)
        for item in data_dict:
            if item == "银行名称":
                self.create.select_bank_name(data_dict[item])
            elif item == "通道主体":
                self.create.select_channel(data_dict[item])
            elif item == "结算主体":
                self.create.select_settle(data_dict[item])
        self.common.click_submit()
