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
xml_obj = xml_utils.XmlUtils(Merchant().read_path("xml", "refund_query"))


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
        self.raw_one = dict_home['RowOne']
        self.status = dict_home['Status']

    # ----- 页面操作 ----- #
    def input_pay_id(self, val):
        # 输入支付 ID
        self.send_keys(self.pay_id, val)

    def click_query(self):
        # 点击查询按钮
        self.click_button(self.query_btn)

    def click_raw(self):
        # 点击第一行
        self.click_button(self.raw_one)

    def get_status(self):
        # 获取处理状态
        return self.get_text(self.status)
