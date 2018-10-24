#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import datetime
from common import basepage
from common import xml_utils
from common.conf_utils import AdminSystem

# 读取 xml 文件
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "risk_monitor"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.pay_id = dict_home['PayId']
        self.counterfeit = dict_home['Counterfeit']
        self.table_menu = dict_home['TableMenu']
        self.table_val = dict_home['TableValue']

    # ----- 页面操作 ----- #
    def input_pay_id(self, val):
        # 输入支付 ID
        self.send_keys(self.pay_id, val)

    def click_counterfeit(self):
        # 点击新增伪冒
        self.click_button(self.counterfeit)

    def get_table_val(self, row, val):
        # 获取表格中的某一行元素
        return self.get_texts(self.table_menu, self.table_val, row, val)


class Create(basepage.Action):
    """
    新增伪冒页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'create', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.pay_id = dict_home['PayId']
        self.reason = dict_home['Reason']

    # ----- 页面操作 ----- #
    def input_pay_id(self, val):
        # 输入支付ID
        self.send_keys(self.pay_id, val)

    def input_uo_time(self):
        # 输入伪冒时间
        data_val = str(datetime.date.today() + datetime.timedelta(60))
        date_str = data_val + " 18:00:00"
        # js 修改默认日期
        self.exec_script("document.getElementById('uoTime').value='{}';".format(date_str))

    def select_reason(self, item):
        # 选择伪冒原因
        self.select_combobox(self.reason, item, "text")
