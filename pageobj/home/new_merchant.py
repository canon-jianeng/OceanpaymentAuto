#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from common import basepage
from common import xml_utils
from common.conf_utils import Merchant

# 读取 xml 文件
xml_obj = xml_utils.XmlUtils(Merchant().read_path("xml", "home"))


class LoginPage(basepage.Action):
    """
    账户后台登录页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'login', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.login_flag = dict_home['LoginFlag']
        self.account = dict_home['Account']
        self.name = dict_home['LoginName']
        self.passwd = dict_home['LoginPass']
        self.check_code = dict_home['CheckCode']
        self.login_btn = dict_home['LoginBtn']

    # ----- 页面操作 ----- #
    def open(self, base_url, page_title):
        # 调用 page 中的 _open 打开链接
        self._open(base_url, page_title)

    def get_login_flag(self):
        return self.is_exist(self.login_btn)

    def input_account(self, val):
        # 输入账户号
        self.send_keys(self.account, val)

    def input_name(self, val):
        # 输入登录名
        self.send_keys(self.name, val)

    def input_passwd(self, val):
        # 输入登录密码
        self.send_keys(self.passwd, val)

    def input_check(self, val=""):
        # 输入图形验证码
        self.send_keys(self.check_code, val)

    def click_login(self):
        # 点击登录按钮
        self.click_button(self.login_btn)


class HomePage(basepage.Action):
    """
    账户后台首页
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'home', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.menu_one = dict_home['MenuOne']
        self.menu_two = dict_home['MenuTwo']
        self.language = dict_home['Language']
        self.chinese = dict_home['Chinese']
        self.confirm = dict_home['ConfirmBtn']

    # ----- 页面操作 ----- #
    def click_menu_one(self, val):
        # 获得一级菜单
        self.click_by_name(self.menu_one, val)

    def click_menu_two(self, val):
        # 获得二级菜单
        self.click_by_name(self.menu_two, val)

    def select_language(self):
        # 选择界面语言
        self.click_button(self.language)
        self.click_button(self.chinese)

    def click_confirm(self):
        # 点击确认
        self.click_button(self.confirm)
