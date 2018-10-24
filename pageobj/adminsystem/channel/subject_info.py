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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "subject_info"))


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
        self.subject = dict_home['Subject']
        self.settle = dict_home['Settle']
        self.create = dict_home['Create']
        self.res_null = dict_home['ResNull']

    # ----- 页面操作 ----- #
    def select_bank_name(self, val):
        # 选择银行名称
        self.click_button(self.name_btn)
        self.send_keys(self.name_input, val)
        self.click_button(self.name_val)

    def select_subject(self, item):
        # 选择通道主体
        self.select_combobox(self.subject, item)

    def select_settle(self, item):
        # 选择结算主体
        self.select_combobox(self.settle, item)

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
        self.name_btn = dict_home['NameBtn']
        self.name_input = dict_home['NameInput']
        self.name_val = dict_home['NameVal']
        self.channel = dict_home['Channel']
        self.settle = dict_home['Settle']

    # ----- 页面操作 ----- #
    def select_bank_name(self, val):
        # 选择银行名称
        self.click_button(self.name_btn)
        self.send_keys(self.name_input, val)
        self.click_button(self.name_val)

    def select_channel(self, item):
        # 选择通道主体
        self.select_combobox(self.channel, item)

    def select_settle(self, item):
        # 选择结算主体
        self.select_combobox(self.settle, item)
