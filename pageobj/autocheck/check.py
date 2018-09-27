#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from common import basepage
from common import xml_utils
from common.conf_utils import AutoCheck

# 读取 xml 文件
xml_obj = xml_utils.XmlUtils(AutoCheck().read_path("xml", "check"))


class Check(basepage.Action):
    """
    对账接口 测试页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'check', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # "提交地址" 下拉框
        self.addr = dict_val['ComboboxAddr']
        # 帐号ID
        self.account = dict_val['AccountId']
        # 终端ID
        self.terminal = dict_val['TerminalId']
        # SecureCode
        self.code = dict_val['SecureCode']
        # OrderNumber
        self.num = dict_val['OrderNumber']
        # "检索交易结果" 按钮
        self.sub = dict_val['Submit']

    # ----- 页面操作 ----- #
    def select_suburl(self, item):
        # 选择 "提交地址" 下拉框
        self.select_combobox(self.addr, item)

    def input_account(self, account):
        # 输入帐号ID
        self.send_keys(self.account, account)

    def input_terminal(self, terminal):
        # 输入终端ID
        self.send_keys(self.terminal, terminal)

    def input_code(self, code):
        # 输入 SecureCode
        self.send_keys(self.code, code)

    def input_num(self, num):
        # 输入 OrderNumber
        self.send_keys(self.num, num)

    def click_submit(self):
        # 点击 "检索交易结果" 按钮
        self.click_button(self.sub)


class Track(basepage.Action):
    """
    物流信息上传接口 测试页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'track', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # "提交地址" 下拉框
        self.addr = dict_val['ComboboxAddr']
        # 帐号ID
        self.account = dict_val['AccountId']
        # 终端ID
        self.terminal = dict_val['TerminalId']
        # SecureCode
        self.code = dict_val['SecureCode']
        # 支付ID
        self.id = dict_val['PayId']
        # "物流信息上传" 按钮
        self.sub = dict_val['Submit']

    # ----- 页面操作 ----- #
    def select_suburl(self, item):
        # 选择 "提交地址" 下拉框
        self.select_combobox(self.addr, item)

    def input_account(self, account):
        # 输入帐号ID
        self.send_keys(self.account, account)

    def input_terminal(self, terminal):
        # 输入终端ID
        self.send_keys(self.terminal, terminal)

    def input_code(self, code):
        # 输入 SecureCode
        self.send_keys(self.code, code)

    def input_id(self, pay_id):
        # 输入支付ID
        self.send_keys(self.id, pay_id)

    def click_submit(self):
        # 点击 "物流信息上传" 按钮
        self.click_button(self.sub)


class ApplyRefund(basepage.Action):
    """
    退款申请接口 测试页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'applyrefund', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # "提交地址" 下拉框
        self.addr = dict_val['ComboboxAddr']
        # 帐号ID
        self.account = dict_val['AccountId']
        # 终端ID
        self.terminal = dict_val['TerminalId']
        # SecureCode
        self.code = dict_val['SecureCode']
        # 支付ID
        self.id = dict_val['PayId']
        # 交易金额
        self.oramo = dict_val['OrderAmount']
        # 退款类型
        self.rety = dict_val['RefundType']
        # 退款金额
        self.reamo = dict_val['RefundAmount']
        # "退款申请" 按钮
        self.sub = dict_val['Submit']

    # ----- 页面操作 ----- #
    def select_suburl(self, item):
        # 选择 "提交地址" 下拉框
        self.select_combobox(self.addr, item)

    def input_account(self, account):
        # 输入帐号ID
        self.send_keys(self.account, account)

    def input_terminal(self, terminal):
        # 输入终端ID
        self.send_keys(self.terminal, terminal)

    def input_code(self, code):
        # 输入 SecureCode
        self.send_keys(self.code, code)

    def input_id(self, pay_id):
        # 输入支付ID
        self.send_keys(self.id, pay_id)

    def input_oramo(self, amount):
        # 输入交易金额
        self.send_keys(self.oramo, amount)

    def select_type(self, item):
        # 选择 "退款类型" 下拉框
        self.select_combobox(self.rety, item)

    def input_reamo(self, amount):
        # 输入退款金额
        self.send_keys(self.reamo, amount)

    def click_submit(self):
        # 点击 "退款申请" 按钮
        self.click_button(self.sub)


class QueryRefund(basepage.Action):
    """
    退款查询接口 测试页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'queryrefund', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # "提交地址" 下拉框
        self.addr = dict_val['ComboboxAddr']
        # 帐号ID
        self.account = dict_val['AccountId']
        # 终端ID
        self.terminal = dict_val['TerminalId']
        # SecureCode
        self.code = dict_val['SecureCode']
        # 退款ID
        self.id = dict_val['RefundId']
        # "检索交易结果" 按钮
        self.sub = dict_val['Submit']

    # ----- 页面操作 ----- #
    def select_suburl(self, item):
        # 选择 "提交地址" 下拉框
        self.select_combobox(self.addr, item)

    def input_account(self, account):
        # 输入帐号ID
        self.send_keys(self.account, account)

    def input_terminal(self, terminal):
        # 输入终端ID
        self.send_keys(self.terminal, terminal)

    def input_code(self, code):
        # 输入 SecureCode
        self.send_keys(self.code, code)

    def input_id(self, refund_id):
        # 输入退款ID
        self.send_keys(self.id, refund_id)

    def click_submit(self):
        # 点击 "检索交易结果" 按钮
        self.click_button(self.sub)
