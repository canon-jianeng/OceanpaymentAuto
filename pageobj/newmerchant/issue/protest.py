#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from common import basepage
from common import xml_utils
from common.conf_utils import Merchant

# 读取 xml 文件
xml_obj = xml_utils.XmlUtils(Merchant().read_path("xml", "protest"))


class Query(basepage.Action):
    """
    查询页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'query', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.pay_id = dict_home['PayId']
        self.query_btn = dict_home['QueryBtn']
        self.appeal_btn = dict_home['AppealBtn']
        self.row = dict_home['Row']

    # ----- 页面操作 ----- #
    def input_pay_id(self, val):
        # 输入支付 ID
        self.send_keys(self.pay_id, val)

    def click_query(self):
        # 点击查询按钮
        self.click_button(self.query_btn)

    def click_appeal_btn(self):
        # 点击发起申诉按钮
        self.click_button(self.appeal_btn)

    def click_row(self):
        # 点击结果行
        self.click_button(self.row)

    def get_ele_color(self, status_val):
        js_val = """
            // RGB 颜色转16进制格式
            function zero_fill_hex(num, digits) {
              var s = num.toString(16);
              while (s.length < digits)
                s = "0" + s;
              return s;
            };
            
            function rgb2hex(rgb) {
              if (rgb.charAt(0) == '#')
                return rgb;
              var ds = rgb.split(/\D+/);
              var decimal = Number(ds[1]) * 65536 + Number(ds[2]) * 256 + Number(ds[3]);
              return "#" + zero_fill_hex(decimal, 6);
            };
        """
        js_str = """
            rgbToHex = function(){{
              var arr = document.getElementsByClassName('label label-primary');
              for(var i=0; i<arr.length; i++){{
                if(arr[i].textContent == '{}'){{
                  return rgb2hex(window.getComputedStyle(arr[i], null)['background-color'])
                }}
              }}
            }};
            return rgbToHex();
        """
        return self.exec_script(js_val+js_str.format(status_val))


class Appeal(basepage.Action):
    """
    申诉页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        dict_home = xml_obj.get_attr_by_tag('pageName', 'appeal', 'locator')

        # ----- 定位器，通过元素属性定位元素对象 ----- #
        self.des_box = dict_home['Descri']
        self.text_area = dict_home['TextArea']
        self.appeal_btn = dict_home['AppealBtn']
        self.appeal_upload = dict_home['AppealUpload']
        self.appeal_submit = dict_home['AppealSubmit']
        self.appeal_success = dict_home['AppealSuccess']
        self.submit = dict_home['Submit']

    # ----- 页面操作 ----- #
    def click_des(self):
        # self.click_button(self.des_box)
        # 滚动到某个元素位置, 点击详细说明复选框
        self.exec_script("document.getElementById('f1').scrollIntoView();"
                         "document.getElementById('f1').click();")

    def input_text_area(self, val):
        # 输入详细说明文本域
        # self.send_keys(self.appeal_btn, val)
        self.exec_script("document.getElementById('a1').value='{}';".format(val))

    def click_appeal(self):
        # 点击上传申诉材料按钮
        self.exec_script("document.getElementById('f1').scrollIntoView();")
        self.click_button(self.appeal_btn)

    def click_upload(self):
        # 点击上传申诉材料 - 上传文件按钮
        self.upload_file(self.appeal_upload, Merchant().read_path("file", "upload_path"))

    def click_appeal_submit(self):
        # 点击上传申诉材料 - 提交按钮
        self.click_button(self.appeal_submit)

    def click_appeal_success(self):
        # 点击上传申诉材料 - 成功按钮
        self.click_button(self.appeal_success)

    def click_submit(self):
        # 点击提交按钮
        # self.click_button(self.submit)
        js_val = """
            // 点击提交按钮
            var arr = document.getElementsByClassName('btn btn-primary');
            for(var i=0; i<arr.length; i++){
                if(arr[i].value == '提交'){
                    arr[i].click()
                }
            };
            // 等待 0.5 秒后, 点击确认
            setTimeout("document.getElementsByClassName('confirm')[0].click()", 500);
            """
        self.exec_script(js_val)
