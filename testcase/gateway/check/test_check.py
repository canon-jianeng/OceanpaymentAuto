#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import unittest
import ddt
from action.autocheck import check as Che
from action.gateway import result as Res
from action.gateway import threepay as Tp
from action.home.gateway import Home
from common.browser import get_driver
from common.conf_utils import Gateway
from common.conf_utils import AutoCheck
from common.excel_utils import ExcelUtils as Exc
from common.logger import Log

# 日志
log = Log()


@ddt.ddt
class TestCheck(unittest.TestCase):
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
        cls.driver.close()

    @ddt.data(*Exc(AutoCheck().read_path("xlsx", "check"), "check").read_merged())
    def test_check(self, test_data):
        # 进入 3方信用卡
        Home(self.driver).enter_postpage("3方信用卡")
        # 提交 3方支付
        Tp.Action(self.driver).put_three(
            test_data["ThreePay"], test_data["PayDomain"],
            self.payval)
        # 获取订单号
        num = Res.Result(self.driver).back_val("order_number")
        # 进入对账接口测试页面
        Home(self.driver).enter_postpage("对账")
        # 对账操作
        Che.Action(self.driver).put_check(test_data["AutoCheck"], num)
        # 断言：测试结果与预期结果对比
        res_dict = test_data["TestResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_tag_val(key_val))

    @ddt.data(*Exc(AutoCheck().read_path("xlsx", "check"), "track").read_merged())
    def test_track(self, test_data):
        # 进入 3方信用卡
        Home(self.driver).enter_postpage("3方信用卡")
        # 提交 3方支付
        Tp.Action(self.driver).put_three(
            test_data["ThreePay"], test_data["PayDomain"],
            self.payval)
        # 获取支付 ID
        pay_id = Res.Result(self.driver).back_val("payment_id")
        # 进入物流上传测试页面
        Home(self.driver).enter_postpage("物流上传")
        # 物流上传操作
        Che.Action(self.driver).put_track(test_data["Track"], pay_id)
        log.info("物流上传结果 signValue：{}".format(Res.Result(self.driver).back_tag_val("signValue")))
        # 断言：测试结果与预期结果对比
        res_dict = test_data["TestResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_tag_val(key_val))

    @ddt.data(*Exc(AutoCheck().read_path("xlsx", "check"), "refund").read_merged())
    def test_refund(self, test_data):
        # 进入 3方信用卡
        Home(self.driver).enter_postpage("3方信用卡")
        # 提交 3方支付
        Tp.Action(self.driver).put_three(
            test_data["ThreePay"], test_data["PayDomain"],
            self.payval)
        # 获取金额
        # amount = Res.Result(self.driver).back_val("order_amount")
        # 获取支付 ID
        pay_id = Res.Result(self.driver).back_val("payment_id")
        # 进入退款申请测试页面
        Home(self.driver).enter_postpage("退款申请")
        # 申请退款操作
        Che.Action(self.driver).apply_refund(test_data["ApplyRefund"], pay_id)
        # 获取退款ID
        refund_id = Res.Result(self.driver).back_tag_val("refund_id")
        log.info("退款ID：{}".format(refund_id))
        # 断言：退款成功
        res_dict = test_data["ApplyResult"]
        for key_val in res_dict:
            return_val = Res.Result(self.driver).back_tag_val(key_val)
            self.assertEqual(res_dict[key_val], return_val)
            if key_val == "refund_description":
                log.info("申请退款结果描述：{}".format(return_val))
        # 进入退款查询测试页面
        Home(self.driver).enter_postpage("退款查询")
        # 查询退款操作
        try:
            Che.Action(self.driver).query_refund(test_data["QueryRefund"], refund_id)
        except TypeError:
            log.error("退款ID为空")
        log.info("查询退款结果描述：{}".format(Res.Result(self.driver).back_tag_val("refund_description")))
        # 断言：测试结果与预期结果对比
        res_dict = test_data["QueryResult"]
        for key_val in res_dict:
            self.assertEqual(res_dict[key_val], Res.Result(self.driver).back_tag_val(key_val))


if __name__ == "__main__":
    unittest.main()
