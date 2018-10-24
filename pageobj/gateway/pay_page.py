#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import datetime
from common import basepage
from common import xml_utils
from common.conf_utils import Gateway

# 当前年份的下一年
YEAR = str(datetime.datetime.now().year + 1)
# 当前月份
if int(datetime.datetime.now().month) > 9:
    MONTH = '{0}'.format(datetime.datetime.now().month)
else:
    MONTH = '0{0}'.format(datetime.datetime.now().month)
# 格式: 月/年 "0119"
MON_YEAR = MONTH + YEAR[2:]

# 读取 xml 文件
xml_obj = xml_utils.XmlUtils(Gateway().read_path("xml", "pay"))


class Pay(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'paypage', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # CardNumber
        self.num = dict_val['CardNumber']
        # "月份" 下拉框
        self.mon = dict_val['ComboboxMonth']
        # "年份" 下拉框
        self.year = dict_val['ComboboxYear']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "PAY_NOW" 按钮
        self.pay = dict_val['PayNow']

    # ----- 页面操作 ----- #
    def loc_frame(self):
        self.switch_frame("index", index=1)

    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def select_card_month(self):
        # 选择 "月份" 下拉框
        self.select_combobox(self.mon, MONTH)

    def select_card_year(self):
        # 选择 "年份" 下拉框
        self.select_combobox(self.year, YEAR, way="value")

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_pay_now(self):
        # 点击 "PAY_NOW" 按钮
        self.click_button(self.pay)


class Starcor(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'starcor', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # CardNumber
        self.num = dict_val['CardNumber']
        # "月份" 文本框
        self.mon = dict_val['ComboboxMonth']
        # "年份" 文本框
        self.year = dict_val['ComboboxYear']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "PAY_NOW" 按钮
        self.pay = dict_val['PayNow']

    # ----- 页面操作 ----- #
    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def input_card_month(self):
        # 输入 "月份" 文本框
        self.send_keys(self.mon, MONTH)

    def input_card_year(self):
        # 输入 "年份" 文本框
        self.send_keys(self.year, YEAR)

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_pay_now(self):
        # 点击 "PAY_NOW" 按钮
        self.click_button(self.pay)


class Standard(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'billingstandardpay', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # CardNumber
        self.num = dict_val['CardNumber']
        # "月份" 下拉框
        self.mon = dict_val['ComboboxMonth']
        # "年份" 下拉框
        self.year = dict_val['ComboboxYear']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "PAY_NOW" 按钮
        self.pay = dict_val['PayNow']

    # ----- 页面操作 ----- #
    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def select_card_month(self):
        # 选择 "月份" 下拉框
        self.select_combobox(self.mon, MONTH)

    def select_card_year(self):
        # 选择 "年份" 下拉框
        self.select_combobox(self.year, YEAR, way="value")

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_pay_now(self):
        # 点击 "PAY_NOW" 按钮
        self.click_button(self.pay)


class Ncgame(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'ncgamepay', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # CardNumber
        self.num = dict_val['CardNumber']
        # "月份" 下拉框
        self.mon = dict_val['ComboboxMonth']
        # "年份" 下拉框
        self.year = dict_val['ComboboxYear']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "Continue" 按钮
        self.con = dict_val['Continue']

    # ----- 页面操作 ----- #
    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def select_card_month(self):
        # 选择 "月份" 下拉框
        self.select_combobox(self.mon, MONTH)

    def select_card_year(self):
        # 选择 "年份" 下拉框
        self.select_combobox(self.year, YEAR, way="value")

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_continue(self):
        # 点击 "Continue" 按钮
        self.click_button(self.con)


class Safe(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'safepay', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # CardNumber
        self.num = dict_val['CardNumber']
        # "月份" 下拉框
        self.mon = dict_val['ComboboxMonth']
        # "年份" 下拉框
        self.year = dict_val['ComboboxYear']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "PAY_NOW" 按钮
        self.pay = dict_val['PayNow']

    # ----- 页面操作 ----- #
    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def select_card_month(self):
        # 选择 "月份" 下拉框
        self.select_combobox(self.mon, MONTH)

    def select_card_year(self):
        # 选择 "年份" 下拉框
        self.select_combobox(self.year, YEAR, way="value")

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_pay_now(self):
        # 点击 "PAY_NOW" 按钮
        self.click_button(self.pay)


class Inst(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'installmentpay', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # CPF/CNPJ
        self.cpf = dict_val['CnpjCpf']
        # CardNumber
        self.num = dict_val['CardNumber']
        # "月份" 下拉框
        self.mon = dict_val['ComboboxMonth']
        # "年份" 下拉框
        self.year = dict_val['ComboboxYear']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "PAY_NOW" 按钮
        self.pay = dict_val['PayNow']

    # ----- 页面操作 ----- #
    def input_cpf(self, cpf):
        # 输入 CPF/CNPJ
        self.send_keys(self.cpf, cpf)

    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def select_card_month(self):
        # 选择 "月份" 下拉框
        self.select_combobox(self.mon, MONTH)

    def select_card_year(self):
        # 选择 "年份" 下拉框
        self.select_combobox(self.year, YEAR, way="value")

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_pay_now(self):
        # 点击 "PAY_NOW" 按钮
        self.click_button(self.pay)


class Multiple(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'multiplepay', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # VISA
        self.visa = dict_val['Visa']
        # CardNumber
        self.cardnum = dict_val['CardNumber']
        # "月份" 下拉框
        self.cardmon = dict_val['ComboboxMonth']
        # "年份" 下拉框
        self.cardyear = dict_val['ComboboxYear']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "PAY_NOW" 按钮
        self.pay_now = dict_val['Continue']

    # ----- 页面操作 ----- #
    def click_visa(self):
        # 输入 VISA
        self.click_button(self.visa)

    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.cardnum, card_number)

    def select_card_month(self):
        # 选择 "月份" 下拉框
        self.select_combobox(self.cardmon, MONTH)

    def select_card_year(self):
        # 选择 "年份" 下拉框
        self.select_combobox(self.cardyear, YEAR, way="value")

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_continue(self):
        # 点击 "PAY_NOW" 按钮
        self.click_button(self.pay_now)


class Quick(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'billingquickpay', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # CardNumber
        self.num = dict_val['CardNumber']
        # "月份"输入框
        self.mon = dict_val['ComboboxMonth']
        # "年份"输入框
        self.year = dict_val['ComboboxYear']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "PAY_NOW" 按钮
        self.pay = dict_val['PayNow']

    # ----- 页面操作 ----- #
    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def input_card_month(self):
        # 输入 "月份"
        self.send_keys(self.mon, MONTH)

    def input_card_year(self):
        # 输入 "年份"
        self.send_keys(self.year, YEAR[2:])

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_pay_now(self):
        # 点击 "PAY_NOW" 按钮
        self.click_button(self.pay)


class Ever(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'evermarkerpay', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # CardNumber
        self.num = dict_val['CardNumber']
        # "年月"输入框
        self.date = dict_val['ExpirationDate']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "PAY_NOW" 按钮
        self.confirm = dict_val['ConfirmPayment']

    # ----- 页面操作 ----- #
    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def input_expiration(self):
        # 输入 "年月"
        self.send_keys(self.date, MON_YEAR)

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_confirm(self):
        # 点击 "PAY_NOW" 按钮
        self.click_button(self.confirm)


class Secure(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'pblsecurepay', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # "同意"复选框
        self.agree = dict_val['ConfirmBox']
        # CardNumber
        self.num = dict_val['CardNumber']
        # "年月"输入框
        self.date = dict_val['ExpirationDate']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "PAY_NOW" 按钮
        self.pay = dict_val['PayNow']

    # ----- 页面操作 ----- #
    def click_agree(self):
        # 点击 "同意"
        self.select_checkbox(self.agree)

    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def input_expiration(self):
        # 输入 "年月"
        self.send_keys(self.date, MON_YEAR)

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_pay_now(self):
        # 点击 "PAY_NOW" 按钮
        self.click_button(self.pay)


class Web(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'webpay', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # CardNumber
        self.num = dict_val['CardNumber']
        # "年月"输入框
        self.date = dict_val['ExpirationDate']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "PAY NOW" 按钮
        self.pay = dict_val['PayNow']

    # ----- 页面操作 ----- #
    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def input_expiration(self):
        # 输入 "年月"
        self.send_keys(self.date, MON_YEAR)

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_pay_now(self):
        # 点击 "PAY NOW" 按钮
        self.click_button(self.pay)


class Virtual(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'virtualpay', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # CPF/CNPJ
        self.cpf = dict_val['CnpjCpf']
        # CardNumber
        self.num = dict_val['CardNumber']
        # "月份" 下拉框
        self.mon = dict_val['ComboboxMonth']
        # "年份" 下拉框
        self.year = dict_val['ComboboxYear']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "Continue" 按钮
        self.con = dict_val['Continue']

    # ----- 页面操作 ----- #
    def input_cpf(self, cpf):
        # 输入 CPF/CNPJ
        self.send_keys(self.cpf, cpf)

    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def select_card_month(self):
        # 选择 "月份" 下拉框
        self.select_combobox(self.mon, MONTH)

    def select_card_year(self):
        # 选择 "年份" 下拉框
        self.select_combobox(self.year, YEAR, way="value")

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_continue(self):
        # 点击 "Continue" 按钮
        self.click_button(self.con)


class WebBr(basepage.Action):
    """
    三方域名支付页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_val = xml_obj.get_attr_by_tag('pageName', 'webbrpay', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # CPF/CNPJ
        self.cpf = dict_val['CnpjCpf']
        # CardNumber
        self.num = dict_val['CardNumber']
        # "年月"输入框
        self.date = dict_val['ExpirationDate']
        # SecureCode
        self.code = dict_val['SecureCode']
        # "PAY NOW" 按钮
        self.pay = dict_val['PayNow']

    # ----- 页面操作 ----- #
    def input_cpf(self, cpf):
        # 输入 CPF/CNPJ
        self.send_keys(self.cpf, cpf)

    def input_card_number(self, card_number):
        # 输入 CardNumber
        self.send_keys(self.num, card_number)

    def input_expiration(self):
        # 输入 "年月"
        self.send_keys(self.date, MON_YEAR)

    def input_secure_code(self, secure_code):
        # 输入 SecureCode
        self.send_keys(self.code, secure_code)

    def click_pay_now(self):
        # 点击 "PAY NOW" 按钮
        self.click_button(self.pay)
