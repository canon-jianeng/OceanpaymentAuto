#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.channel import channel_param as Tra
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

    def query_param(self, method, bank, channel):
        log.info("查询通道参数配置")
        Home(self.driver).channel_param()
        time.sleep(0.5)
        self.query.select_pay_method(method)
        self.query.select_bank_name(bank)
        self.query.select_channel_name(channel)
        self.common.click_query()
        time.sleep(0.5)
        res = self.query.get_res_null()
        if res == "没有找到相关记录，请重新输入条件进行查询 .":
            return res
        return ""

    def create_param(self, data_dict):
        log.info("创建通道参数配置")
        Home(self.driver).channel_param()
        time.sleep(0.5)
        self.query.click_create()
        time.sleep(0.5)
        text_list = ["参数值1", "参数值2", "参数值3", "参数值4", "参数值5",
                     "参数值5", "参数值6", "参数值7", "参数值8", "MPI特殊参数1",
                     "MPI特殊参数2", "MPI特殊参数3", "MPI特殊参数4",
                     "MPI特殊参数5", "备注"]
        select_list = ["支付方式", "银行名称", "通道名称", "通道币种"]
        for item in data_dict:
            if item in select_list:
                self.create.select_item(item, data_dict[item])
            elif item in text_list:
                self.create.input_text(item, data_dict[item])
        self.common.click_submit()
