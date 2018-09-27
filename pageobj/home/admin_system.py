#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from common import basepage
from common import xml_utils
from common.conf_utils import AdminSystem

# 读取 xml 文件
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "home"))


class LoginPage(basepage.Action):
    """
    管理后台登录页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'login', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.name = dict_home['LoginName']
        self.passwd = dict_home['LoginPass']
        self.rand_code = dict_home['RandCode']
        self.phone_code = dict_home['PhoneCode']
        self.login_btn = dict_home['LoginBtn']

    # ----- 页面操作 ----- #
    def open(self, base_url, page_title):
        # 调用page中的_open打开链接
        self._open(base_url, page_title)

    def input_name(self, val):
        # 输入登录名
        self.send_keys(self.name, val)

    def input_passwd(self, val):
        # 输入登录密码
        self.send_keys(self.passwd, val)

    def input_rand(self, val):
        # 输入图形验证码
        self.send_keys(self.rand_code, val)

    def input_phone(self, val):
        # 输入短信验证码
        self.send_keys(self.phone_code, val)

    def click_login(self):
        # 点击登录按钮
        self.click_button(self.login_btn)


class HomePage(basepage.Action):
    """
    管理后台首页
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'home', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.menu_one = dict_home['MenuOne']
        self.menu_two = dict_home['MenuTwo']

    # ----- 页面操作 ----- #
    def switch_left(self):
        # 切换到左侧导航栏
        self.switch_frame("main")
        self.switch_frame("id", "mainFrame")
        self.switch_frame("id", "leftFrame")

    def switch_main(self):
        # 切换到主页面
        self.switch_frame("main")
        self.switch_frame("id", "mainFrame")
        self.switch_frame("id", "main")

    def switch_top(self):
        # 切换到顶部导航栏
        self.switch_frame("main")
        self.switch_frame("name", "topFrame")

    def click_menu(self, val_one, val_two):
        # 进入一级菜单 - 二级菜单
        self.click_btn(self.menu_one, val_one)
        time.sleep(0.5)
        self.click_btn(self.menu_two, val_two)


class Common(basepage.Action):
    """
    管理后台公共元素
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'common', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.query = dict_home['QueryBtn']
        self.submit = dict_home['SubmitBtn']
        self.mids = dict_home['Mids']
        self.table_menu = dict_home['TableMenu']
        self.table_val = dict_home['TableValue']
        self.account_name = dict_home['AccountName']
        self.quit_btn = dict_home['QuitBtn']
        self.login_name = dict_home['LoginName']

    # ----- 页面操作 ----- #
    def click_query(self):
        # 点击查询按钮
        self.click_button(self.query)

    def click_submit(self):
        # 点击提交按钮
        self.click_button(self.submit)

    def click_mids(self):
        # 点击单(复)选框
        self.click_button(self.mids)

    def get_table_val(self, row, val):
        # 获取表格中的某一行元素
        return self.get_texts(self.table_menu, self.table_val, row, val)

    def get_account_name(self):
        # 获取账户名称
        return self.get_text(self.account_name)

    def click_quit(self):
        # 点击退出按钮
        self.click_button(self.quit_btn)

    def click_confirm(self):
        # 点击确定
        self.confirm_alert()

    def get_login_flag(self):
        # 判断登录名标签是否存在
        return self.is_exist(self.login_name)
