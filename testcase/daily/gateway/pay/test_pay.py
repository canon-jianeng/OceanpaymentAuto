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
from action.gateway import threepay as Tp
from action.gateway import threequick as Tq
from action.gateway import twopay as Twp
from action.gateway import twoquick as Twq
from action.gateway import twohalfpay as Thp
from action.gateway import twohalfquick as Thq
from action.gateway import sendtrade as St
from action.gateway import moto as Mo
from action.gateway import result as Res
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
        pass

    def tearDown(self):
        pass

    @ddt.data(*Exc(Gateway().read_data("pay"), "ThreePay").read_merged())
    def test_threepay(self, test_data):
        # 进入 3方信用卡
        Home(self.driver).enter_postpage("3方信用卡")
        # 提交 3方支付
        Tp.Action(self.driver).put_three(
            test_data["ThreePay"], test_data["PayDomain"],
            self.payval)
        # 断言：3方信用卡交易成功
        res_dict = test_data["TestResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_val(key_val))

    @ddt.data(*Exc(Gateway().read_data("pay"), "ThreeQuick").read_merged())
    def test_threequick(self, test_data):
        # 进入 quick 3方
        Home(self.driver).enter_postpage("quick3方")
        # 创建订单
        Tq.Action(self.driver).put_create(
            test_data["ThreeQuick"], test_data["PayDomain"],
            self.payval)
        # 获取 quickpay_id
        quick_id = Res.Result(self.driver).back_val("quickpay_id")
        # 进入 quick 3方
        Home(self.driver).enter_postpage("quick3方")
        # 支付订单
        Tq.Action(self.driver).put_pay(test_data["ThreeQuick"], quick_id)
        # 断言：quick 3方交易成功
        res_dict = test_data["TestResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_check(key_val))

    @ddt.data(*Exc(Gateway().read_data("pay"), "TwoPay").read_merged())
    def test_two(self, test_data):
        # 进入 2方信用卡
        Home(self.driver).enter_postpage("2方信用卡")
        # 提交 2方支付
        Twp.Action(self.driver).put_two(test_data["TestData"])
        # 断言：2方信用卡交易成功
        res_dict = test_data["TestResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_tag_val(key_val))

    @ddt.data(*Exc(Gateway().read_data("pay"), "TwoQuick").read_merged())
    def test_twoquick(self, test_data):
        # 进入 quick 2方
        Home(self.driver).enter_postpage("quick2方")
        # 创建订单
        Twq.Action(self.driver).put_create(test_data["TestData"])
        # 获取 quickpay_id
        quick_id = Res.Result(self.driver).back_tag_val("quickpay_id")
        self.driver.back()
        # 支付订单
        Twq.Action(self.driver).put_pay(test_data["TestData"], quick_id)
        # 断言：quick 2方交易成功
        res_dict = test_data["TestResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_tag_val(key_val))

    @ddt.data(*Exc(Gateway().read_data("pay"), "TwoHalfPay").read_merged())
    def test_twohalf(self, test_data):
        # 进入 2.5方信用卡
        Home(self.driver).enter_postpage("2.5方支付")
        # 提交 2.5方支付
        Thp.Action(self.driver).put_twohalf(test_data["TestData"])
        # 断言：2.5方信用卡交易成功
        res_dict = test_data["TestResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_val(key_val))

    @unittest.skip("正式环境没有这个接口, 跳过此用例")
    @ddt.data(*Exc(Gateway().read_data("pay"), "TwoHalfQuick").read_merged())
    def test_twohalfquick(self, test_data):
        # 进入 quick 2.5方
        Home(self.driver).enter_postpage("quick2.5方")
        # 创建订单
        Thq.Action(self.driver).put_create(test_data["TestData"])
        # 获取 quickpay_id
        quick_id = Res.Result(self.driver).back_val("quickpay_id")
        self.driver.back()
        # 支付订单
        Thq.Action(self.driver).put_pay(test_data["TestData"], quick_id)
        # 断言：quick 2.5方交易成功
        res_dict = test_data["TestResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_tag_val(key_val))

    @ddt.data(*Exc(Gateway().read_data("moto"), "Moto").read_merged())
    def test_moto(self, test_data):
        # 进入 moto
        Home(self.driver).enter_postpage("MOTO")
        # moto 测试
        Mo.Action(self.driver).moto(test_data["TestData"])
        # 断言：MoTo 交易成功
        res_dict = test_data["TestResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_tag_val(key_val))

    @ddt.data(*Exc(Gateway().read_data("pay"), "SendTrade").read_merged())
    def test_send_trade(self, test_data):
        # 进入创建订单接口
        Home(self.driver).enter_postpage("创建订单接口")
        # 创建订单
        St.Action(self.driver).create_trade(test_data["ThreePay"])
        # 断言：创建订单成功
        res_dict = test_data["CreateResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_tag_val(key_val))
        pay_url = Res.Result(self.driver).back_tag_val("pay_url")
        # 支付订单
        St.Action(self.driver).pay_trade(test_data["PayDomain"], pay_url, self.payval)
        # 断言：创建订单支付成功
        res_dict = test_data["TestResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_val(key_val))


if __name__ == "__main__":
    unittest.main()
