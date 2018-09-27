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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "abnormal_apply"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.pay_id = dict_home['PayId']
        self.draw_back = dict_home['DrawBack']
        self.ref_pay = dict_home['RefusalPay']
        self.freeze = dict_home['Freeze']
        self.apply = dict_home['ApplyBtn']

    # ----- 页面操作 ----- #
    def input_pay_id(self, val):
        # 输入支付 ID
        self.send_keys(self.pay_id, val)

    def select_draw_back(self, item):
        # 选择退款状态
        self.select_combobox(self.draw_back, item)

    def select_ref_pay(self, item):
        # 选择拒付状态
        self.select_combobox(self.ref_pay, item)

    def select_freeze(self, item):
        # 选择调单状态
        self.select_combobox(self.freeze, item)

    def click_apply(self):
        # 点击申请
        self.click_button(self.apply)


class Apply(basepage.Action):
    """
    申请页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'apply', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.sub_type = dict_home['SubmitType']
        self.abn_type = dict_home['AbnormalType']
        self.amount = dict_home['Amount']
        self.arn = dict_home['ARN']
        self.repaly_time = dict_home['RepalyTime']
        self.protest_reason = dict_home['ProtestReason']
        self.reason = dict_home['Reason']

    # ----- 页面操作 ----- #
    def select_sub_type(self, item):
        # 选择提交人类型
        self.select_combobox(self.sub_type, item, "text")

    def select_abn_type(self, item):
        # 选择异常类型
        self.select_combobox(self.abn_type, item, "text")

    def input_amount(self, val):
        # 输入异常金额
        self.send_keys(self.amount, val)

    def input_arn(self):
        # 输入标识码ARN
        self.send_keys(self.arn, 1)

    def input_repaly_time(self):
        # 输入回复截止时间
        data_val = str(datetime.date.today() + datetime.timedelta(60))
        date_str = data_val + " 18:00:00"
        # js 去除 readonly 属性
        # self.exec_script('document.getElementById("repalytime").removeAttribute("readonly");')
        # self.send_keys(self.repaly_time, date_str)
        # js 修改默认日期
        self.exec_script("document.getElementById('repalytime').value='{}';".format(date_str))

    def select_protest_reason(self, item):
        # 选择拒付原因
        self.select_combobox(self.protest_reason, item, "text")

    def input_reason(self, val):
        # 输入异常原因
        self.send_keys(self.reason, val)
