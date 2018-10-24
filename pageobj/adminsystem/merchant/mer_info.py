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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "mer_info"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.mer_no = dict_home['MerNo']
        self.active = dict_home['Active']
        self.assign = dict_home['AssignLimit']

    # ----- 页面操作 ----- #
    def input_mer_no(self, val):
        # 输入账户
        self.send_keys(self.mer_no, val)

    def click_active(self):
        # 点击激活
        self.click_button(self.active)

    def click_assign(self):
        # 点击分配权限
        self.click_button(self.assign)


class Assign(basepage.Action):
    """
    分配权限页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'assign', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.all = dict_home['AllLimit']

    # ----- 页面操作 ----- #
    def click_all(self):
        # 点击全部权限
        self.click_button(self.all)
