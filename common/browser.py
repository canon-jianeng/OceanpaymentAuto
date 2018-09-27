#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from selenium import webdriver


def get_driver():
    """  浏览器运行模式 """
    # 无界面运行
    # 配置浏览器参数
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # return webdriver.Chrome(chrome_options=options)
    # 图形界面运行
    return webdriver.Chrome()
