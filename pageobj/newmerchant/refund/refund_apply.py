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
xml_obj = xml_utils.XmlUtils(Merchant().read_path("xml", "refund_apply"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'apply', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.order_num = dict_home['OrderNum']
        self.pay_id = dict_home['PayId']
        self.refund_part = dict_home['RefundPart']
        self.refund_amount = dict_home['RefundAmount']
        self.refund_reason = dict_home['RefundReason']
        self.refund_des = dict_home['RefundDes']
        self.refund_info = dict_home['RefundInfo']
        self.submit = dict_home['Submit']

    # ----- 页面操作 ----- #
    def input_order_num(self, val):
        # 输入账户订单号
        self.send_keys(self.order_num, val)

    def input_pay_id(self, val):
        # 输入支付 ID
        self.send_keys(self.pay_id, val)

    def click_part(self):
        # 点击部分退款
        self.click_button(self.refund_part)

    def input_amount(self, val):
        # 输入退款金额
        self.send_keys(self.refund_amount, val)

    def select_reason(self, item):
        # 选择退款原因
        self.select_combobox(self.refund_reason, item, way="text")

    def input_refund_des(self, val="test"):
        # 输入退款说明
        self.send_keys(self.refund_des, val)

    def input_refund_info(self, val="test"):
        # 输入退款附加信息
        self.send_keys(self.refund_info, val)

    def click_submit(self):
        # 点击提交按钮
        self.click_button(self.submit)
