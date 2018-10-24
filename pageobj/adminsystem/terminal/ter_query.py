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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "ter_query"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.mer_no = dict_home['MerNo']
        self.terminal = dict_home['Terminal']
        self.create = dict_home['Create']
        self.modify = dict_home['Modify']
        self.start = dict_home['Start']
        self.active = dict_home['Active']
        self.res_null = dict_home['ResNull']

    # ----- 页面操作 ----- #
    def input_mer_no(self, val):
        # 输入账户
        self.send_keys(self.mer_no, val)

    def input_terminal(self, val):
        # 输入终端号
        self.send_keys(self.terminal, val)

    def click_create(self):
        # 点击新增
        self.click_button(self.create)

    def click_modify(self):
        # 点击修改
        self.click_button(self.modify)

    def click_start(self):
        # 点击启用
        self.click_button(self.start)

    def click_active(self):
        # 点击激活
        self.click_button(self.active)

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
        self.secure_code = dict_home['SecureCode']
        self.inf_type = dict_home['InfType']
        self.bus_type = dict_home['BusType']
        self.ip_check_no = dict_home['IpCheckNo']
        self.pay_times = dict_home['PayTimes']
        self.return_model = dict_home['ReturnModel']

    # ----- 页面操作 ----- #
    def input_mer_no(self, val):
        # 输入账户
        self.send_keys(self.mer_no, val)

    def input_secure_code(self, val):
        # 输入 secureCode
        self.send_keys(self.secure_code, val)

    def select_inf_type(self, item):
        # 选择绑定接口类型
        self.select_combobox(self.inf_type, item)

    def select_bus_type(self, item):
        # 选择行业类型
        self.select_combobox(self.bus_type, item)

    def click_ip_no(self):
        # 不校验 ip 地址
        self.click_button(self.ip_check_no)

    def input_pay_times(self, val="-1"):
        # 支付频繁次数
        self.send_keys(self.pay_times, val)

    def select_model(self, item):
        # 选择返回类型
        self.select_combobox(self.return_model, item)


class Modify(basepage.Action):
    """
    修改页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'modify', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.secure_code = dict_home['SecureCode']
        self.inf_type = dict_home['InfType']
        self.bus_type = dict_home['BusType']
        self.ip_check_no = dict_home['IpCheckNo']
        self.pay_times = dict_home['PayTimes']
        self.return_model = dict_home['ReturnModel']

    # ----- 页面操作 ----- #
    def input_secure_code(self, val):
        # 输入 secureCode
        self.send_keys(self.secure_code, val)

    def select_inf_type(self, item):
        # 选择绑定接口类型
        self.select_combobox(self.inf_type, item)

    def select_bus_type(self, item):
        # 选择行业类型
        self.select_combobox(self.bus_type, item)

    def click_ip_no(self):
        # 不校验 ip 地址
        self.click_button(self.ip_check_no)

    def input_pay_times(self, val="-1"):
        # 支付频繁次数
        self.send_keys(self.pay_times, val)

    def select_model(self, item):
        # 选择返回类型
        self.select_combobox(self.return_model, item)
