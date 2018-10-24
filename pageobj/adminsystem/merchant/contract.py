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
xml_obj = xml_utils.XmlUtils(AdminSystem().read_path("xml", "contract"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.mer_no = dict_home['MerNo']
        self.create = dict_home['Create']
        self.verify = dict_home['Verify']

    # ----- 页面操作 ----- #
    def input_mer_no(self, val):
        # 输入账户
        self.send_keys(self.mer_no, val)

    def click_create(self):
        # 点击新增
        self.click_button(self.create)

    def click_verify(self):
        # 点击复核
        self.click_button(self.verify)


class Create(basepage.Action):
    """
    新增页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'create', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.mer_no = dict_home['MerNo']
        self.mer_text = dict_home['MerNoText']
        self.mer_select = dict_home['MerNoSelect']
        self.auto_renew = dict_home['AutoRenew']
        self.contract_type = dict_home['ContractType']

    # ----- 页面操作 ----- #
    def input_mer_no(self, val):
        # 输入账户
        self.click_button(self.mer_no)
        self.send_keys(self.mer_text, val)
        self.click_button(self.mer_select)

    def select_init_date(self):
        # 合同起始日期
        data_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        init_js = "document.getElementById('coPactstdateST').value='{}';"
        self.exec_script(init_js.format(data_now))

    def select_end_date(self):
        # 合同结束日期
        data_val = str(datetime.date.today() + datetime.timedelta(60))
        date_str = data_val + " 18:00:00"
        end_js = "document.getElementById('coPactendateED').value='{}';"
        self.exec_script(end_js.format(date_str))

    def click_auto_renew(self):
        # 点击自动续约
        self.click_button(self.auto_renew)

    def select_contract_type(self, item):
        # 选择合同类型
        self.select_combobox(self.contract_type, item)

    def select_start_date(self):
        # 生效时间
        data_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        start_js = "document.getElementById('merEffectDate').value='{}';"
        self.exec_script(start_js.format(data_now))


class Verify(basepage.Action):
    """
    复核页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'verify', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.status = dict_home['Status']

    # ----- 页面操作 ----- #
    def select_status(self, item):
        # 选择复核状态
        self.select_combobox(self.status, item)
