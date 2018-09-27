#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import pageobj.gateway.result_page as Res


class Result(object):
    """
    结果页面
    """
    def __init__(self, driver):
        self.driver = driver

    def back_val(self, tag_name):
        return Res.ResultObj(self.driver).return_val(tag_name)

    def back_tag_val(self, tag_name):
        return Res.ResultObj(self.driver).return_tagval(tag_name)

    def back_check(self, tag_name):
        return Res.ResultObj(self.driver).return_check(tag_name)
