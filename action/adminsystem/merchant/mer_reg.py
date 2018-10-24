#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import datetime
from pageobj.adminsystem.merchant import mer_reg as Tra
from pageobj.home.admin_system import Common
from action.home.admin_system import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.register = Tra.Register(driver)
        self.common = Common(driver)
        self.driver = driver

    def create_account(self):
        log.info("创建账户")
        Home(self.driver).merchant_reg()
        name = "auto" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.register.input_acc(name)
        self.register.input_newpass("admin123")
        self.register.input_repass("admin123")
        self.register.input_mer_name(name)
        self.register.select_busid("商户行业")
        self.register.input_merman(name)
        self.register.input_merphone("18695669842")
        self.register.input_merfax("775040818")
        self.register.input_mer_website("www.oceanpayment.com.cn")
        self.register.input_mer_email("canon@oceanpayment.com.cn")
        self.register.input_mer_sales(name)
        self.common.click_submit()
