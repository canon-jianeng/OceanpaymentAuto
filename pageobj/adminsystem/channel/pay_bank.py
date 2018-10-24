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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "pay_bank"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.bank_code = dict_home['BankCode']
        self.create = dict_home['Create']
        self.res_null = dict_home['ResNull']

    # ----- 页面操作 ----- #
    def input_bank_code(self, val):
        # 输入账户
        self.send_keys(self.bank_code, val)

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
        self.radio_yes = dict_home['RadioYes']
        self.radio_no = dict_home['RadioNo']
        self.check_name = dict_home['CheckName']
        self.check_box = dict_home['Checkbox']
        self.item_global = dict_home['Global']

    # ----- 页面操作 ----- #
    def input_text(self, name, val):
        # 输入文本
        self.exec_actions(self.var_name, self.text, name, "input", val)

    def select_item(self, name, val):
        # 选择下拉框
        self.exec_actions(self.var_name, self.select, name, "select", val)

    def click_radio(self, name, flag):
        # 点击单选按钮
        if flag == "是":
            self.exec_actions(self.var_name, self.radio_yes, name, "click")
        else:
            self.exec_actions(self.var_name, self.radio_no, name, "click")

    def click_bank_country(self, name):
        # 选择支持国家
        if name == "全球":
            self.click_button(self.item_global)
        else:
            self.exec_actions(self.check_name, self.check_box, name, "click")
