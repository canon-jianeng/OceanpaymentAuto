#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import unittest
import ddt
from common.browser import get_driver
from common.excel_utils import ExcelUtils as Exc
from common.logger import Log
from common.conf_utils import Gateway
from common.conf_utils import Merchant
from action.gateway import threepay as Tp
from action.gateway import result as Res
from action.home.new_merchant import Home as Nmh
from action.home.admin_system import Home as Ash
from action.adminsystem.trade_info import abnormal_query as Aq
from action.newmerchant.refund import refund_apply as Ra
from action.newmerchant.refund import refund_query as Rq
from action.home.gateway import Home

# 日志
log = Log()


@ddt.ddt
class TestGateway(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 浏览器驱动
        cls.driver = get_driver()
        log.info("----- 启动浏览器 -----")
        # 浏览器最大化
        cls.driver.maximize_window()
        # 获取支付域名列表数据
        cls.payval = Gateway().read_domain("domain")

    @classmethod
    def tearDownClass(cls):
        log.info("----- 关闭浏览器 -----")
        cls.driver.quit()

    def setUp(self):
        # 账户后台账号
        self.nm_account = "160135"
        self.nm_name = "autotest"
        self.nm_pwd = "admin123"
        # 管理后台
        self.as_name = "canon"
        self.as_pwd = "Neng2018"
        self.as_tname = "canon1"
        self.as_tpwd = "Neng2018"

    def tearDown(self):
        pass

    @ddt.data(*Exc(Merchant().read_data("issue"), "refund").read_merged())
    def test_refund(self, test_data):
        # 进入 3方信用卡
        Home(self.driver).enter_postpage("3方信用卡")
        # 提交 3方支付
        Tp.Action(self.driver).put_three(
            test_data["ThreePay"], test_data["PayDomain"],
            self.payval)
        # 断言: 判断三方支付成功
        res_dict = test_data["PayResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_val(key_val))
        pay_id = Res.Result(self.driver).back_val("payment_id")
        order_num = Res.Result(self.driver).back_val("order_number")
        # 登录账户后台
        Nmh(self.driver).login(self.nm_account, self.nm_name, self.nm_pwd)
        # 申请退款
        Ra.Action(self.driver).apply_refund(
            order_num, pay_id,
            test_data["ThreePay"]["交易金额"],
            test_data["Refund"]["amount"]
        )
        # 登录管理后台
        Ash(self.driver).login(self.as_name, self.as_pwd)
        # 审核
        Aq.Action(self.driver).query_abn_type(pay_id, "退款")
        Aq.Action(self.driver).review()
        # 断言: 判断审核状态
        Aq.Action(self.driver).query_abn_type(pay_id, "退款")
        abn_status = Aq.Action(self.driver).get_query_result("审核状态")
        self.assertEqual("审核成功未处理", abn_status)
        # 更换账号, 登录管理后台
        Ash(self.driver).login(self.as_tname, self.as_tpwd)
        Ash(self.driver).abn_apply()
        # 复核
        Aq.Action(self.driver).query_abn_type(pay_id, "退款")
        Aq.Action(self.driver).verify()
        # 断言: 判断审核状态
        Aq.Action(self.driver).query_abn_type(pay_id, "退款")
        abn_status = Aq.Action(self.driver).get_query_result("审核状态")
        self.assertEqual("审核成功已处理", abn_status)
        # 登录账户后台
        Nmh(self.driver).login(self.nm_account, self.nm_name, self.nm_pwd)
        # 断言: 判断退款处理状态
        handle_status = Rq.Action(self.driver).query_status(pay_id).strip()
        self.assertEqual("成功", handle_status)
