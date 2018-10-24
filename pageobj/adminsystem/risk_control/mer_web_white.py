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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "mer_web_white"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.terminal = dict_home['Terminal']
        self.create = dict_home['Create']
        self.review = dict_home['Review']
        self.verify = dict_home['Verify']
        self.res_null = dict_home['ResNull']

    # ----- 页面操作 ----- #
    def input_terminal(self, val):
        # 输入终端号
        self.send_keys(self.terminal, val)

    def click_create(self):
        # 点击新增
        self.click_button(self.create)

    def click_review(self):
        # 点击审核
        self.click_button(self.review)

    def click_verify(self):
        # 点击复核
        self.click_button(self.verify)

    def get_res_null(self):
        # 获取查询结果
        return self.is_exist(self.res_null)


class Create(basepage.Action):
    """
    新增页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'create', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.mer_no = dict_home['MerNo']
        self.terminal = dict_home['Terminal']
        self.websit = dict_home['Websit']

    # ----- 页面操作 ----- #
    def input_mer_no(self, val):
        # 输入账户
        self.send_keys(self.mer_no, val)
        self.click_blank()

    def click_terminal(self, val):
        # 输入终端号
        self.click_button(self.terminal, val)

    def input_websit(self, val):
        # 输入支付网址
        self.send_keys(self.websit, val)
