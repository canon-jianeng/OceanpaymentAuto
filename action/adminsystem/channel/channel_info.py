#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import time
from pageobj.adminsystem.channel import channel_info as Tra
from pageobj.home.admin_system import Common
from action.home.admin_system import Home
from common.logger import Log

log = Log()


class Action(object):
    def __init__(self, driver):
        self.query = Tra.Query(driver)
        self.create = Tra.Create(driver)
        self.common = Common(driver)
        self.driver = driver

    def query_channel(self, name):
        log.info("查询通道信息")
        Home(self.driver).channel_info()
        time.sleep(0.5)
        self.query.select_channel_name(name)
        return self.query.is_val()

    def get_channel_info(self, name, item):
        log.info("获取通道信息: {}".format(item))
        Home(self.driver).channel_info()
        time.sleep(0.5)
        self.query.select_channel_name(name, flag=True)
        self.common.click_query()
        return self.common.get_table_val("1", item)

    def create_channel(self, data_dict):
        log.info("创建通道")
        Home(self.driver).channel_info()
        time.sleep(0.5)
        self.query.click_create()
        time.sleep(0.5)
        text_list = ["通道名称", "通道账户", "自动对账用户名", "自动对账用户密码",
                     "通道进入码", "通道安全码", "预留一", "预留二", "账单地址",
                     "MCC", "账单地址白名单", "账单地址附加值1", "账单地址附加值1白名单",
                     "账单地址附加值2", "最小交易金额", "最大交易金额", "结算银行",
                     "通道后台管理员账号", "通道后台管理员密码", "单笔手续费金额",
                     "通道保证金比率", "通道标识", "备注"]
        radio_list = ["银行通道是否为3方接口", "是否支持DCC", "是否延时通道", "是否支持3方接口",
                      "是否支持2.5方接口", "是否支持2方接口", "是否支持退款", "是否支持部分退款",
                      "是否支持部分拒付", "是否支持预授权", "是否3D通道", "是否启用我司自有MPI",
                      "跳转银行付款链接", "是否支持撤销", "失败订单是否收取手续费",
                      "结算前成功订单全额异常是否收取手续费", "结算后成功订单全额异常是否收取手续费",
                      "结算前是否收取异常金额的手续费", "结算后是否收取异常金额的手续费"]
        select_list = ["银行名称", "最小(大)交易金额币种", "单笔手续费币种", "通道主体"]
        for item in data_dict:
            if item in text_list:
                self.create.input_text(item, data_dict[item])
            elif item in radio_list:
                self.create.click_radio(item, data_dict[item])
            elif item in select_list:
                self.create.select_item(item, data_dict[item])
            elif item == "卡种扣率":
                item_rate = data_dict[item].split(",")
                for rate_val in item_rate:
                    self.create.select_rate(rate_val)
            elif item == "通道币种":
                item_mutli = data_dict[item].split(",")
                if len(item_mutli) > 1:
                    self.create.click_cur_type("多币种")
                    time.sleep(0.5)
                    for str_val in item_mutli:
                        self.create.select_mutli_currency(str_val)
                else:
                    # self.create.click_cur_type("单币种")
                    self.create.select_single_currency(item_mutli[0])
        self.common.click_submit()
