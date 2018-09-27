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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "abnormal_query"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.pay_id = dict_home['PayId']
        self.abn_type = dict_home['AbnType']
        self.abn_item = dict_home['AbnItem']
        self.review = dict_home['Review']
        self.verify = dict_home['Verify']

    # ----- 页面操作 ----- #
    def input_pay_id(self, val):
        # 输入支付 ID
        self.send_keys(self.pay_id, val)

    def select_abn_type(self, item):
        # 选择异常类型
        self.select_ul(self.abn_type, self.abn_item, item)

    def click_review(self):
        # 点击审核
        self.click_button(self.review)

    def click_verify(self):
        # 点击复核
        self.click_button(self.verify)


class Review(basepage.Action):
    """
    审核页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'review', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.status = dict_home['CheckStatus']

    # ----- 页面操作 ----- #
    def select_status(self, item):
        # 选择审核状态
        self.select_combobox(self.status, item)


class Verify(basepage.Action):
    """
    复核页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'verify', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.status = dict_home['checkAgainStatus']

    # ----- 页面操作 ----- #
    def select_status(self, item):
        # 选择复核状态
        self.select_combobox(self.status, item)
