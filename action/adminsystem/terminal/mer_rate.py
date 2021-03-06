#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.terminal import mer_rate as Tra
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

    def query_rate(self, terminal, channel, card_type):
        log.info("扣率管理: 查询终端号和卡种")
        Home(self.driver).mer_rate()
        time.sleep(0.5)
        self.query.input_terminal(terminal)
        # 选择通道
        self.query.select_channel(channel.split("(")[0])
        # 不存在扣率的卡种
        lack_list = []
        for val in card_type.split(","):
            val_str = val.strip()
            log.info("卡种: {}".format(val_str))
            self.query.select_card_type(val_str)
            self.common.click_query()
            time.sleep(0.5)
            # 判断是否存在此终端号和卡种的扣率
            res = self.query.get_res_null()
            if res == "没有找到相关记录，请重新输入条件进行查询 .":
                lack_list.append(val_str)
        return lack_list

    def create_rate(self, account, terminal, paymethod,
                    card_type, bank_code, channel, trade_rate):
        log.info("新增扣率管理")
        Home(self.driver).mer_rate()
        time.sleep(0.5)
        self.query.click_create()
        time.sleep(2)
        self.create.input_mer_no(account)
        self.create.select_terminal(terminal)
        self.create.select_pay_method(paymethod)
        self.create.select_card_type(card_type)
        self.create.select_bank(bank_code)
        self.create.select_channel(channel)
        self.create.input_rate(trade_rate)
        self.common.click_submit()
        self.common.confirm_alert()
