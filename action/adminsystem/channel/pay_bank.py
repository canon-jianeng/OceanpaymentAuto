#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.channel import pay_bank as Tra
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

    def query_paybank(self, code):
        log.info("查询支付银行")
        Home(self.driver).pay_bank()
        time.sleep(0.5)
        self.query.input_bank_code(code)
        self.common.click_query()
        time.sleep(0.5)
        res = self.query.get_res_null()
        if res == "没有找到相关记录，请重新输入条件进行查询 .":
            return res
        return ""

    def create_paybank(self, data_dict):
        log.info("创建支付银行")
        Home(self.driver).pay_bank()
        time.sleep(0.5)
        self.query.click_create()
        time.sleep(0.5)
        text_list = ["银行代码", "银行名称", "银行支付URL", "银行自动对账URL",
                     "银行退款URL", "银行校验URL", "银行后台管理网址", "提交地址",
                     "对账地址", "接收地址", "退款地址", "调用方法名", "备注"]
        radio_list = ["是否直连", "是否参与结算", "是否开启交易监控", "是否支持退款"]
        select_list = ["支付方式"]
        for item in data_dict:
            if item in text_list:
                self.create.input_text(item, data_dict[item])
            elif item in radio_list:
                self.create.click_radio(item, data_dict[item])
            elif item in select_list:
                self.create.select_item(item, data_dict[item])
            elif item == "支持国家":
                for str_val in data_dict[item].split(","):
                    self.create.click_bank_country(str_val)
        self.common.click_submit()
