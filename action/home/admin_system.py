#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from pageobj.home.admin_system import LoginPage
from pageobj.home.admin_system import HomePage
from pageobj.home.admin_system import Common
from common.conf_utils import AdminSystem
from common.logger import Log
import time

log = Log()


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.login_obj = LoginPage(self.driver)
        self.home_obj = HomePage(self.driver)
        self.common = Common(self.driver)

    def login(self, name, pwd):
        url = AdminSystem().read_link()
        self.login_obj.open(url, "管理后台")
        # 判断用户是否登录
        val = self.common.get_login_flag()
        if not val:
            # 退出账号
            self.home_obj.switch_top()
            self.common.click_quit()
            self.common.click_confirm()
        self.login_obj.input_name(name)
        self.login_obj.input_passwd(pwd)
        self.login_obj.input_rand("")
        self.login_obj.click_login()
        self.login_obj.input_phone("111111")
        self.login_obj.click_login()
        log.info("{} 登录管理后台".format(name))

    def formal_query(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("交易信息管理", "正式交易查询")
        self.home_obj.switch_main()
        log.info("进入交易信息管理 - 正式交易查询")

    def abn_query(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("交易信息管理", "异常交易查询")
        self.home_obj.switch_main()
        log.info("进入交易信息管理 - 异常交易查询")

    def abn_apply(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("交易信息管理", "异常交易申请")
        self.home_obj.switch_main()
        log.info("进入交易信息管理 - 异常交易申请")
