#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from common import basepage
from common import xml_utils
from common.conf_utils import Gateway

# 读取 xml 文件
xml_obj = xml_utils.XmlUtils(Gateway().read_path("xml", "home"))


class HomePage(basepage.Action):
    """
    支付网关首页
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'testpage', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        # 接口名称
        self.link = dict_home['Interface']

    # ----- 页面操作 ----- #
    def open(self, base_url, page_title):
        # 调用page中的_open打开链接
        self._open(base_url, page_title)

    def click_interface(self, value):
        # 点击接口链接
        self.click_by_name(self.link, value)
