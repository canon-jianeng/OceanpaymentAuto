#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from common import basepage
from common import xml_utils
from common.conf_utils import Merchant

# 读取 xml 文件
xml_obj = xml_utils.XmlUtils(Merchant().read_path("xml", "freeze"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.pay_id = dict_home['PayId']
        self.query_btn = dict_home['QueryBtn']
        self.refund_btn = dict_home['RefundBtn']
        self.row = dict_home['Row']
        self.confirm = dict_home['Confirm']

    # ----- 页面操作 ----- #
    def input_pay_id(self, val):
        # 输入支付 ID
        self.send_keys(self.pay_id, val)

    def click_query(self):
        # 点击查询按钮
        self.click_button(self.query_btn)

    def click_refund_btn(self):
        # 点击 "接收退款" 按钮
        self.click_button(self.refund_btn)

    def click_row(self):
        # 点击结果行
        self.click_button(self.row)

    def click_confirm(self):
        # 点击 "确认" 按钮
        self.click_button(self.confirm)
