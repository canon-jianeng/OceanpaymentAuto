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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "pay_method"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.pay_name = dict_home['PayName']
        self.create = dict_home['Create']
        self.res_null = dict_home['ResNull']

    # ----- 页面操作 ----- #
    def input_pay_name(self, val):
        # 输入账户
        self.send_keys(self.pay_name, val)

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
        self.tag_name = dict_home['TagName']
        self.tag_text = dict_home['TagText']
        self.method_btn = dict_home['MethodBtn']
        self.method_name = dict_home['MethodName']

    # ----- 页面操作 ----- #
    def input_text(self, name, val):
        # 输入文本框
        self.exec_actions(self.tag_name, self.tag_text, name, "input", val)

    def select_pay_method(self, name):
        # 选择支付方式类别
        self.exec_actions(self.method_name, self.method_btn, name, "click")
