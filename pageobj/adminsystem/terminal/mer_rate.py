#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from common import basepage
from common import xml_utils
from common.conf_utils import AdminSystem

# 读取 xml 文件
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "mer_rate"))


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
        self.channel_btn = dict_home['ChannelBtn']
        self.channel = dict_home['Channel']
        self.card_btn = dict_home['CardBtn']
        self.not_all = dict_home['AllNot']
        self.card_type = dict_home['CardType']
        self.res_null = dict_home['ResNull']

    # ----- 页面操作 ----- #
    def input_terminal(self, val):
        # 输入终端号
        self.send_keys(self.terminal, val)

    def select_channel(self, item):
        # 点击通道下拉框
        self.click_button(self.channel_btn)
        # 点击对应的通道
        self.click_by_name(self.channel, item)

    def select_card_type(self, item):
        # 点击卡种下拉框
        self.click_button(self.card_btn)
        time.sleep(0.5)
        # 点击全不选
        self.click_button(self.not_all)
        # 点击对应的卡种
        self.click_by_name(self.card_type, item)

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
        self.pay_method = dict_home['PayMethod']
        self.card_btn = dict_home['CardBtn']
        self.card_total = dict_home['CardTotal']
        self.bank_btn = dict_home['BankBtn']
        self.bank_item = dict_home['BankItem']
        self.channel_btn = dict_home['Channelbtn']
        self.channel_item = dict_home['ChannelItem']
        self.trade_rate = dict_home['TradeRate']

    # ----- 页面操作 ----- #
    def input_mer_no(self, val):
        # 输入账户
        self.send_keys(self.mer_no, val)
        self.click_blank()

    def select_terminal(self, item):
        # 输入终端号
        self.select_combobox(self.terminal, item, way="value")

    def select_pay_method(self, item):
        # 输入支付方式
        self.select_combobox(self.pay_method, item)

    def select_card_type(self, card_type):
        # 选择卡种
        self.click_button(self.card_btn)
        card_var = []
        if isinstance(card_type, str):
            card_var = card_type.split(",")
        elif isinstance(card_type, list):
            card_var = card_type
        for val in card_var:
            self.click_by_name(self.card_total, val.strip())
        self.click_button(self.card_btn)

    def select_bank(self, bank_code):
        # 选择银行代码
        self.click_button(self.bank_btn)
        self.click_button(self.bank_item, bank_code)

    def select_channel(self, channel):
        # 选择通道
        self.click_button(self.channel_btn)
        self.click_button(self.channel_item, channel)

    def input_rate(self, trade_rate):
        # 输入交易扣率
        self.send_keys(self.trade_rate, trade_rate)
