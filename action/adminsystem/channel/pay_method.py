#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.channel import pay_method as Tra
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

    def query_pay_method(self, pay_name):
        log.info("查询支付方式")
        Home(self.driver).pay_method()
        time.sleep(0.5)
        self.query.input_pay_name(pay_name)
        self.common.click_query()
        time.sleep(0.5)
        res = self.query.get_res_null()
        if res == "没有找到相关记录，请重新输入条件进行查询 .":
            return res
        return ""

    def create_pay_method(self, data_dict):
        log.info("创建支付方式")
        Home(self.driver).pay_method()
        time.sleep(0.5)
        self.query.click_create()
        time.sleep(0.5)
        text_list = ["支付名称", "显示名称", "支付链接", "附加支付链接",
                     "校验URL", "Logo Url", "排序", "备注"]
        for item in data_dict:
            if item == "支付方式类别":
                self.create.select_pay_method(data_dict[item])
            else:
                for text in text_list:
                    if item == text:
                        self.create.input_text(item, data_dict[item])
        self.common.click_submit()
