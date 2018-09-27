#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from pageobj.home.new_merchant import LoginPage
from pageobj.home.new_merchant import HomePage
from common.conf_utils import Merchant
from common.logger import Log

log = Log()


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.login_obj = LoginPage(self.driver)
        self.home_obj = HomePage(self.driver)

    def login(self, account, name, pwd):
        url = Merchant().read_link()
        try:
            self.login_obj.open(url, "支付平台-账户后台")
            login_flag = True
        except Exception:
            self.login_obj.open(url, "Oceanpayment | 首页")
            login_flag = False
        if login_flag:
            self.login_obj.input_account(account)
            self.login_obj.input_name(name)
            self.login_obj.input_passwd(pwd)
            self.login_obj.input_check("")
            self.login_obj.click_login()
        log.info("登录账户后台")

    def click_meun(self, first, second):
        self.home_obj.click_menu_one(first)
        self.home_obj.click_menu_two(second)
        log.info("进入{} - {}".format(first, second))
