#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.home.admin_system import LoginPage
from pageobj.home.admin_system import HomePage
from pageobj.home.admin_system import Common
from common.conf_utils import AdminSystem
from common.logger import Log

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

    def get_res(self):
        time.sleep(1)
        return self.common.get_sub_res().strip()

    def merchant_reg(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("账户管理", "账户注册")
        self.home_obj.switch_main()
        log.info("进入账户管理 - 账户注册")

    def merchant_info(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("账户管理", "账户信息管理")
        self.home_obj.switch_main()
        log.info("进入账户管理 - 账户信息管理")

    def merchant_contract(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("账户管理", "合同信息管理")
        self.home_obj.switch_main()
        log.info("进入账户管理 - 合同信息管理")

    def terminal_query(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("终端号管理", "查询终端号")
        self.home_obj.switch_main()
        log.info("进入终端号管理 - 查询终端号")

    def terminal_to_channel(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("终端号管理", "查询终端号通道绑定")
        self.home_obj.switch_main()
        log.info("进入终端号管理 - 查询终端号通道绑定")

    def mer_rate(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("终端号管理", "扣率管理")
        self.home_obj.switch_main()
        log.info("进入终端号管理 - 扣率管理")

    def pay_method(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("通道管理", "支付方式管理")
        self.home_obj.switch_main()
        log.info("进入通道管理 - 支付方式管理")

    def pay_bank(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("通道管理", "支付银行信息管理")
        self.home_obj.switch_main()
        log.info("进入通道管理 - 支付银行信息管理")

    def channel_info(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("通道管理", "通道信息管理")
        self.home_obj.switch_main()
        log.info("进入通道管理 - 通道信息管理")

    def channel_param(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("通道管理", "通道特殊参数配置")
        self.home_obj.switch_main()
        log.info("进入通道管理 - 通道特殊参数配置")

    def subject_info(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("通道管理", "主体信息管理")
        self.home_obj.switch_main()
        log.info("进入通道管理 - 主体信息管理")

    def mer_domain(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("支付域名管理", "账户域名绑定管理")
        self.home_obj.switch_main()
        log.info("进入支付域名管理 - 账户域名绑定管理")

    def agent_info(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("代理商管理", "代理商信息管理")
        self.home_obj.switch_main()
        log.info("进入代理商管理 - 代理商信息管理")

    def agent_merchant(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("代理商管理", "代理商账户管理")
        self.home_obj.switch_main()
        log.info("进入代理商管理 - 代理商账户管理")

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

    def merweb_white(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("风控管理", "来源网址白名单信息管理")
        self.home_obj.switch_main()
        log.info("进入风控管理 - 来源网址白名单信息管理")

    def risk_monitor(self):
        self.home_obj.switch_left()
        self.home_obj.click_menu("风控管理", "风险监控综合管理")
        self.home_obj.switch_main()
        log.info("进入风控管理 - 风险监控综合管理")
