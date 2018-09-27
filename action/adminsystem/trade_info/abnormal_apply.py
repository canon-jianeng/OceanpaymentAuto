#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from pageobj.adminsystem.trade_info import abnormal_apply as Tra
from pageobj.home.admin_system import Common
from action.home.admin_system import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.common = Common(driver)
        self.query = Tra.Query(driver)
        self.apply = Tra.Apply(driver)
        self.driver = driver

    def apply_protest(self, pay_id, sub_type, abn_type, amount, protest):
        # 查询支付ID
        Home(self.driver).abn_apply()
        self.query.input_pay_id(pay_id)
        self.common.click_query()
        # 申请拒付
        self.common.click_mids()
        self.query.click_apply()
        self.apply.select_sub_type(sub_type)
        self.apply.select_abn_type(abn_type)
        self.apply.input_amount(amount)
        self.apply.input_arn()
        self.apply.input_repaly_time()
        self.apply.select_protest_reason(protest)
        self.common.click_submit()
        log.info("申请拒付")

    def apply_freeze(self, pay_id, sub_type, abn_type, amount):
        # 查询支付ID
        Home(self.driver).abn_apply()
        self.query.input_pay_id(pay_id)
        self.common.click_query()
        # 申请调单
        self.common.click_mids()
        self.query.click_apply()
        self.apply.select_sub_type(sub_type)
        self.apply.select_abn_type(abn_type)
        self.apply.input_amount(amount)
        self.apply.input_arn()
        self.apply.input_repaly_time()
        self.apply.input_reason("autotest")
        self.common.click_submit()
        log.info("申请调单")

    def apply_appeal_success(self, pay_id, sub_type, abn_type):
        # 查询支付ID
        Home(self.driver).abn_apply()
        self.query.input_pay_id(pay_id)
        self.common.click_query()
        # 申请申诉成功
        self.common.click_mids()
        self.query.click_apply()
        self.apply.select_sub_type(sub_type)
        self.apply.select_abn_type(abn_type)
        self.common.click_submit()
        log.info("申请申诉成功")

    def query_refund(self, pay_id, refund):
        Home(self.driver).abn_apply()
        self.query.input_pay_id(pay_id)
        self.query.select_draw_back(refund)
        self.common.click_query()
        log.info("查询支付ID和退款状态")

    def query_protest(self, pay_id, protest):
        Home(self.driver).abn_apply()
        self.query.input_pay_id(pay_id)
        self.query.select_ref_pay(protest)
        self.common.click_query()
        log.info("查询支付ID和拒付状态")

    def query_freeze(self, pay_id, freeze):
        Home(self.driver).abn_apply()
        self.query.input_pay_id(pay_id)
        self.query.select_freeze(freeze)
        self.common.click_query()
        log.info("查询支付ID和调单状态")
