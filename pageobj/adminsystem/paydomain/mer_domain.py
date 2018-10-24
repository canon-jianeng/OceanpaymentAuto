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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "mer_domain"))


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
        self.res_null = dict_home['ResNull']

    # ----- 页面操作 ----- #
    def input_terminal(self, val):
        # 输入终端号
        self.send_keys(self.terminal, val)

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
        self.mer_no = dict_home['MerNo']
        self.terminal = dict_home['Terminal']
        self.md_name = dict_home['MdName']
        self.client_type = dict_home['ClientType']

    # ----- 页面操作 ----- #
    def input_mer_no(self, val):
        # 输入账户
        self.send_keys(self.mer_no, val)
        self.click_blank()

    def select_terminal(self, item):
        # 选择终端号
        self.select_combobox(self.terminal, item)

    def select_md_name(self, item):
        # 选择域名名称
        self.select_combobox(self.md_name, item)

    def select_client_type(self, item):
        # 选择客户端类型
        self.select_combobox(self.client_type, item)
