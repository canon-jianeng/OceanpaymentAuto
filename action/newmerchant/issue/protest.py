#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.newmerchant.issue import protest as Tra
from action.home.new_merchant import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.appeal = Tra.Appeal(driver)
        self.query = Tra.Query(driver)
        self.driver = driver

    def query_pay_id(self, pay_id):
        Home(self.driver).click_meun("问题管理", "拒付处理")
        self.query.input_pay_id(pay_id)
        self.query.click_query()
        time.sleep(1)
        self.query.click_row()
        log.info("查询支付ID")

    def appeal_protest(self, pay_id, text_val, action):
        self.query_pay_id(pay_id)
        # 发起申诉
        self.query.click_appeal_btn()
        if action == "select":
            # 勾选详细说明
            self.appeal.click_des()
            self.appeal.input_text_area(text_val)
        elif action == "upload":
            # 上传申诉材料
            time.sleep(0.5)
            self.appeal.click_appeal()
            self.appeal.click_upload()
            self.appeal.click_appeal_submit()
            self.appeal.click_appeal_success()
        self.appeal.click_submit()
        time.sleep(0.5)
        log.info("发起申诉")

    def get_status_color(self, pay_id, status):
        # 获取状态颜色
        self.query_pay_id(pay_id)
        rgb_hex = self.query.get_ele_color(status)
        log.info("RGB 十六进制值: {}".format(rgb_hex))
        return rgb_hex
