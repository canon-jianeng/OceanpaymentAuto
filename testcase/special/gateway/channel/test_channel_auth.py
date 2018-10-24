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
from action.gateway import auth
from action.autocheck import check as Che
from action.gateway import threepay as Tp
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

    @ddt.data(*Exc(Gateway().read_data("channel"), "Auth").read_merged())
    def test_auth(self, test_data):
        # 进入 3方信用卡
        Home(self.driver).enter_postpage("3方信用卡")
        # 提交 3方支付
        Tp.Action(self.driver).put_three(
            test_data["ThreePay"], test_data["PayDomain"],
            self.payval)
        # 获取订单号
        num = Res.Result(self.driver).back_val("order_number")
        # 获取支付 ID
        pay_id = Res.Result(self.driver).back_val("payment_id")
        # 断言：交易状态
        res_dict = test_data["PayResult"]
        for key_val in res_dict:
            self.assertEqual(
                res_dict[key_val],
                Res.Result(self.driver).back_val(key_val), "交易状态错误"
            )
        # 进入预授权
        Home(self.driver).enter_postpage("预授权")
        auth.Action(self.driver).auth(test_data["Auth"], pay_id, num)
        # 断言：预授权成功
        res_dict = test_data["AuthResult"]
        for key_val in res_dict:
            self.assertEqual(
                res_dict[key_val],
                Res.Result(self.driver).back_tag_val(key_val), "预授权操作失败"
            )


if __name__ == "__main__":
    unittest.main()
