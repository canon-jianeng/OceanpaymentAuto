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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "channel_info"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.name_btn = dict_home['NameBtn']
        self.name_input = dict_home['NameInput']
        self.name_val = dict_home['NameVal']
        self.create = dict_home['Create']
        self.res_null = dict_home['ResNull']

    # ----- 页面操作 ----- #
    def select_channel_name(self, val, flag=False):
        # 选择通道名称
        self.click_button(self.name_btn)
        self.send_keys(self.name_input, val)
        if flag:
            self.click_button(self.name_val)

    def is_val(self):
        return self.is_exist(self.name_val)

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
        self.single = dict_home['CurrencySingle']
        self.rate_item = dict_home['RateItem']
        self.rate_single = dict_home['RateSingle']
        self.multi = dict_home['CurrencyMulti']
        self.currency_name = dict_home['CurrencyName']
        self.currency_btn = dict_home['CurrencyBtn']
        self.mutli_name = dict_home['MutliName']
        self.mutli_btn = dict_home['MutliBtn']

    # ----- 页面操作 ----- #
    def input_text(self, name, val):
        # 输入文本框
        self.exec_actions(self.var_name, self.text, name, "input", val)

    def select_item(self, name, val):
        # 选择下拉值
        self.exec_actions(self.var_name, self.select, name, "select", val)

    def click_radio(self, name, flag):
        # 点击单选按钮
        if flag == "是":
            self.exec_actions(self.var_name, self.radio_yes, name, "click")
        else:
            self.exec_actions(self.var_name, self.radio_no, name, "click")

    def click_cur_type(self, flag):
        # 点击币种类型
        if flag == "单币种":
            self.click_button(self.single)
        else:
            self.click_button(self.multi)

    def select_rate(self, name):
        # 选择卡种扣率
        self.exec_actions(self.rate_item, self.rate_single,
                          name, "click")

    def select_single_currency(self, name):
        # 选择单个币种
        self.exec_actions(self.currency_name, self.currency_btn,
                          name, "click")

    def select_mutli_currency(self, name):
        # 选择多个币种
        self.exec_actions(self.mutli_name, self.mutli_btn,
                          name, "click")
