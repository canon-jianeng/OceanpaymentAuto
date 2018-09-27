#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from common.logger import Log
from common.conf_utils import Gateway
from pageobj.home import gateway as Hp

log = Log()


class Home(object):
    def __init__(self, driver):
        url = Gateway().read_link()
        self.driver = driver
        log.info("登录支付网关-首页")
        self.home_obj = Hp.HomePage(self.driver)
        self.home_obj.open(url, "支付平台测试")

    def enter_postpage(self, val):
        self.home_obj.click_interface(val)
        log.info("点击 '{}' 链接".format(val))
