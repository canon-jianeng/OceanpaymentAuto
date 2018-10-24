#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from common import basepage
from common import xml_utils
from common.conf_utils import AdminSystem

# 读取 xml 文件
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "mer_reg"))


class Register(basepage.Action):
    """
    注册页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'register', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.login_acc = dict_home['LoginAccount']
        self.new_pass = dict_home['NewPass']
        self.renew_pass = dict_home['RenewPass']
        self.mer_name = dict_home['MerName']
        self.bus_id = dict_home['BusId']
        self.mer_man = dict_home['MerLinkman']
        self.mer_phone = dict_home['MerLinkphone']
        self.mer_fax = dict_home['MerFax']
        self.mer_website = dict_home['MerWebsite']
        self.mer_email = dict_home['MerEmail']
        self.mer_sales = dict_home['MerSales']

    # ----- 页面操作 ----- #
    def input_acc(self, val):
        # 输入登录账号
        self.send_keys(self.login_acc, val)

    def input_newpass(self, val):
        # 输入登录密码
        self.send_keys(self.new_pass, val)

    def input_repass(self, val):
        # 输入确认密码
        self.send_keys(self.renew_pass, val)

    def input_mer_name(self, val):
        # 输入账户名称
        self.send_keys(self.mer_name, val)

    def select_busid(self, val):
        # 选择所属行业
        self.select_combobox(self.bus_id, val)

    def input_merman(self, val):
        # 输入联系人
        self.send_keys(self.mer_man, val)

    def input_merphone(self, val):
        # 输入联系电话
        self.send_keys(self.mer_phone, val)

    def input_merfax(self, val):
        # 输入QQ
        self.send_keys(self.mer_fax, val)

    def input_mer_website(self, val):
        # 输入公司网址
        self.send_keys(self.mer_website, val)

    def input_mer_email(self, val):
        # 输入邮箱地址
        self.send_keys(self.mer_email, val)

    def input_mer_sales(self, val):
        # 输入销售人员
        self.send_keys(self.mer_sales, val)
