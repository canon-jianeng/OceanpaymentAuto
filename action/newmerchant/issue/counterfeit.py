#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from pageobj.newmerchant.issue import counterfeit as Cou
from action.home.new_merchant import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Cou.Query(driver)
        self.driver = driver

    def query_pay_id(self, pay_id):
        Home(self.driver).click_meun("问题管理", "伪冒处理")
        self.query.input_pay_id(pay_id)
        self.query.click_query()
        self.query.click_row()
        log.info("查询支付ID")

    def get_status_color(self, pay_id, status):
        # 获取状态颜色
        self.query_pay_id(pay_id)
        rgb_hex = self.query.get_ele_color(status)
        log.info("RGB 十六进制值: {}".format(rgb_hex))
        return rgb_hex
