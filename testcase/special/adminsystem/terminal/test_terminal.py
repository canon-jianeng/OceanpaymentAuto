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
from common.conf_utils import AdminSystem
from action.home.admin_system import Home as Ash
from action.adminsystem.merchant import mer_reg as Mer
from action.adminsystem.merchant import mer_info as Mei
from action.adminsystem.agent import agent_mer as Agm
from action.adminsystem.merchant import contract as Con
from action.adminsystem.terminal import terminal_query as Teq
from action.adminsystem.terminal import mer_rate as Mra
from action.adminsystem.terminal import terminal_to_channel as Tec
from action.adminsystem.paydomain import mer_domain as Med
from action.adminsystem.risk_control import mer_web_white as Wew

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

    @classmethod
    def tearDownClass(cls):
        log.info("----- 关闭浏览器 -----")
        cls.driver.quit()

    def setUp(self):
        # 管理后台
        self.as_name = "canon"
        self.as_pwd = "Neng2018"
        self.as_tname = "canon1"
        self.as_tpwd = "Neng2018"

    def tearDown(self):
        pass

    @ddt.data(*Exc(AdminSystem().read_data("terminal"), "merchant").read_merged())
    def test_terminal(self, test_data):
        ac_no = test_data["TestData"]["账户"]
        tm_no = test_data["TestData"]["终端号"]
        inf_type = test_data["TestData"]["接口类型"]
        card_type = test_data["TestData"]["卡种"]
        pay_method = test_data["TestData"]["支付方式"]
        bank_code = test_data["TestData"]["银行代码"]
        channel = test_data["TestData"]["通道"]
        trade_rate = test_data["TestData"]["交易扣率"]
        # 登录管理后台
        Ash(self.driver).login(self.as_name, self.as_pwd)
        # 新增账户号
        if ac_no == "":
            Mer.Action(self.driver).create_account()
            ac_no = Mei.Action(self.driver).get_account()
            tm_no = ac_no + "01"
        # 激活账户
        status_val = Mei.Action(self.driver).query_account(ac_no)
        if status_val == "0":
            Mei.Action(self.driver).assign_roles(ac_no)
            Mei.Action(self.driver).active_account(ac_no)
        # 新增账户绑定代理商 (账户绑定一次)
        agent = Agm.Action(self.driver).query_agent(ac_no)
        if agent:
            Agm.Action(self.driver).create_agent(ac_no, tm_no)
            # 断言: 操作成功
            self.assertEqual("新增代理商账户成功", Ash(self.driver).get_res())
        # 新增合同信息 (账户绑定一次)
        contract = Con.Action(self.driver).query_contract(ac_no)
        if not contract:
            Con.Action(self.driver).create_contract(ac_no)
            # 断言: 操作成功
            self.assertEqual("操作成功", Ash(self.driver).get_res())
        # 复核合同信息
        contract = Con.Action(self.driver).query_contract(ac_no)
        if contract == "1":
            # 登录复核账号
            Ash(self.driver).login(self.as_tname, self.as_tpwd)
            # 复核
            Con.Action(self.driver).verify_contract(ac_no)
            # 登录审核账号
            Ash(self.driver).login(self.as_name, self.as_pwd)
        # 新增终端号
        if tm_no != "":
            log.info(tm_no)
            res = Teq.Action(self.driver).query_terminal(tm_no)
            if res:
                Teq.Action(self.driver).create_terminal(ac_no, inf_type)
                # 断言: 新增成功
                self.assertEqual("操作成功 您的终端号为 : {}".format(tm_no), Ash(self.driver).get_res())
            else:
                return_type = Teq.Action(self.driver).query_list(tm_no, "状态类型")
                if return_type != "推送和正常返回":
                    Teq.Action(self.driver).modify_terminal(tm_no, inf_type)
                    # 断言: 修改成功
                    self.assertEqual("操作成功", Ash(self.driver).get_res())
        else:
            Teq.Action(self.driver).create_terminal(ac_no, inf_type)
            # 断言: 新增成功
            self.assertIn("操作成功", Ash(self.driver).get_res())
            tm_no = Teq.Action(self.driver).get_terminal(ac_no)
        # 新增扣率
        rate_card = Mra.Action(self.driver).query_rate(tm_no, channel, card_type)
        if rate_card:
            Mra.Action(self.driver).create_rate(
                ac_no, tm_no, pay_method,
                rate_card, bank_code, channel, trade_rate
            )
            # 断言: 操作成功
            self.assertEqual("新增扣率成功", Ash(self.driver).get_res())
        # 新增终端号通道绑定
        channel_card = Tec.Action(self.driver).query_channel(tm_no, channel, card_type)
        if channel_card:
            Tec.Action(self.driver).bind_channel(
                ac_no, tm_no, pay_method,
                channel_card, bank_code, channel)
            # 断言: 操作成功
            self.assertEqual("操作成功", Ash(self.driver).get_res())
        # 新增支付域名
        if Med.Action(self.driver).query_domain(tm_no):
            Med.Action(self.driver).create_domain(ac_no, tm_no, '完整版')
            # 断言: 操作成功
            self.assertEqual("新增账户域名绑定成功！", Ash(self.driver).get_res())
        # 激活终端号
        status = Teq.Action(self.driver).query_list(tm_no, "状态")
        if status == "未激活":
            Teq.Action(self.driver).active_terminal(tm_no)
            # 断言: 终端号状态为正常
            self.assertEqual(
                "测试",
                Teq.Action(self.driver).query_list(tm_no, "状态"))
        # 新增来源网址白名单
        if Wew.Action(self.driver).query_web_white(tm_no):
            Wew.Action(self.driver).create_web_white(ac_no, tm_no)
            # 断言: 操作成功
            self.assertEqual("操作成功", Ash(self.driver).get_res())
        # 审核来源网址白名单
        if Wew.Action(self.driver).query_web_white(tm_no) == "0":
            Wew.Action(self.driver).review_web_white(tm_no)
        # 复核来源网址白名单
        if Wew.Action(self.driver).query_web_white(tm_no) == "1":
            # 登录其他账号
            Ash(self.driver).login(self.as_tname, self.as_tpwd)
            Wew.Action(self.driver).verify_web_white(tm_no)
        # 启用终端号
        status = Teq.Action(self.driver).query_list(tm_no, "状态")
        if status == "测试":
            Teq.Action(self.driver).start_terminal(tm_no)
            # 断言: 终端号状态为正常
            self.assertEqual(
                "正常",
                Teq.Action(self.driver).query_list(tm_no, "状态"))
