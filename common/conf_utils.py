#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import os
from configparser import ConfigParser

# 项目路径
CUR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Project(object):
    def __init__(self):
        self.conf = ConfigParser()
        # 读取项目的配置文件
        self.conf.read(CUR_PATH + "/data/config/project.conf", encoding='UTF-8')

    def read_gateway(self):
        return CUR_PATH + self.conf.get("conf", "gateway")

    def read_check(self):
        return CUR_PATH + self.conf.get("conf", "autocheck")

    def read_admin_system(self):
        return CUR_PATH + self.conf.get("conf", "adminsystem")

    def read_merchant(self):
        return CUR_PATH + self.conf.get("conf", "newmerchant")

    def read_log(self):
        """
        读取日志的配置文件
        :return:
        """
        return CUR_PATH + self.conf.get("log", "path")


class Gateway(object):
    def __init__(self):
        self.conf = ConfigParser()
        # 读取支付网关的配置文件
        self.conf.read(Project().read_gateway(), encoding='UTF-8')

    def read_link(self):
        # 读取支付网关登录链接
        return self.conf.get("gateway", "login")

    def read_domain(self, section):
        """
        读取支付域名名称
        :meth section: 支付域名名称 type: str
        :return: 包含元组的列表
        """
        return self.conf.items(section)

    def read_path(self, sec, opt):
        return CUR_PATH + self.conf.get(sec, opt)

    def read_val(self, sec, opt):
        return self.conf.get(sec, opt)


class AutoCheck(object):
    def __init__(self):
        self.conf = ConfigParser()
        # 读取对账的配置文件
        self.conf.read(Project().read_check(), encoding='UTF-8')

    def read_path(self, sec, opt):
        return CUR_PATH + self.conf.get(sec, opt)

    def read_val(self, sec, opt):
        return self.conf.get(sec, opt)


class AdminSystem(object):
    def __init__(self):
        self.conf = ConfigParser()
        # 读取管理后台的配置文件
        self.conf.read(Project().read_admin_system(), encoding='UTF-8')

    def read_link(self):
        # 读取管理后台登录链接
        return self.conf.get("admin_system", "login")

    def read_path(self, sec, opt):
        return CUR_PATH + self.conf.get(sec, opt)

    def read_val(self, sec, opt):
        return self.conf.get(sec, opt)


class Merchant(object):
    def __init__(self):
        self.conf = ConfigParser()
        # 读取管理后台的配置文件
        self.conf.read(Project().read_merchant(), encoding='UTF-8')

    def read_link(self):
        # 读取账户后台登录链接
        return self.conf.get("merchant", "login")

    def read_path(self, sec, opt):
        return CUR_PATH + self.conf.get(sec, opt)

    def read_val(self, sec, opt):
        return self.conf.get(sec, opt)


if __name__ == '__main__':
    val = Gateway().read_domain("domain")
    print(val)
