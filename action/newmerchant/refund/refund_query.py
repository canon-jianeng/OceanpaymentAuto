#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from pageobj.newmerchant.refund import refund_query as Tra
from action.home.new_merchant import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Tra.Query(driver)
        self.driver = driver

    def query_status(self, pay_id):
        Home(self.driver).click_meun("退款管理", "查询退款")
        self.query.input_pay_id(pay_id)
        self.query.click_query()
        log.info("查询退款状态")
        return self.query.get_status()
