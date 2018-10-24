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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "channel_param"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.method_btn = dict_home['MethodBtn']
        self.method_input = dict_home['MethodInput']
        self.method_val = dict_home['MethodVal']
        self.bank_btn = dict_home['BankBtn']
        self.bank_input = dict_home['BankInput']
        self.bank_val = dict_home['BankVal']
        self.name_btn = dict_home['NameBtn']
        self.name_input = dict_home['NameInput']
        self.name_val = dict_home['NameVal']
        self.create = dict_home['Create']
        self.res_null = dict_home['ResNull']

    # ----- 页面操作 ----- #
    def select_pay_method(self, val):
        # 选择支付方式
        self.click_button(self.method_btn)
        self.send_keys(self.method_input, val)
        self.click_button(self.method_val)

    def select_bank_name(self, val):
        # 选择银行名称
        self.click_button(self.bank_btn)
        self.send_keys(self.bank_input, val)
        self.click_button(self.bank_val)

    def select_channel_name(self, val):
        # 选择通道名称
        self.click_button(self.name_btn)
        self.send_keys(self.name_input, val.split("(")[0])
        self.click_button(self.name_val)

    def click_create(self):
        # 点击新增
        self.click_button(self.create)

    def get_res_null(self):
        # 查询结果为空
        return self.is_exist(self.res_null)


class Create(basepage.Action):
    """
    新增页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'create', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.var_name = dict_home['VarName']
        self.text = dict_home['Text']
        self.select = dict_home['Select']

    # ----- 页面操作 ----- #
    def input_text(self, name, val):
        # 输入文本框
        self.exec_actions(self.var_name, self.text, name, "input", val)

    def select_item(self, name, val):
        # 选择下拉值
        self.exec_actions(self.var_name, self.select, name, "select", val)
