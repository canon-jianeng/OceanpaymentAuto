#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from common import basepage


class SubmitPage(basepage.Action):
    """
    支付网关 交易请求页面
    """
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)

    def update_info(self, name, val):
        func_val = """
            function getval(tag_name, item){
              var arr = document.getElementsByTagName('td');
              var first_val = arr[0].textContent.trim();
              for(var i=0; i<arr.length; i=i+2){
                if (!first_val && i == 0){
                  i = 1;
                };
                var name = arr[i].textContent.trim().replace(":", "").replace("：", "");
                if (name == tag_name){
                  var tag = arr[i+1].lastElementChild.tagName;
                  if (tag == "SELECT"){
                    var ele = arr[i+1].lastElementChild;
                    // 选中 select 某一选项
                    arr[i+1].onclick = function(){
                      for (var n = 0; n < ele.options.length; n++){  
                        if (ele.options[n].textContent.trim() == item.trim()){
                          // ele.value=ele.options[n].value;
                          ele.options[n].selected=true;
                          break;
                        };
                      };
                    };
                    arr[i+1].click();
                    return tag;
                  }else{
                    arr[i+1].children[0].value = item;
                    // console.log(arr[i+1].children[0].value);
                    return tag;
                  };
                  break;
                };
              };
            };"""
        call_val = "return getval('{}', '{}');"
        js_val = func_val + call_val.format(name, val)
        return self.exec_script(js_val)

    def click_submit(self, name):
        js_val = """
            var arr = document.getElementsByTagName('td');
            var ele_obj = arr[arr.length-1].children[0];
            if (ele_obj.value == "{}"){{
              ele_obj.click();
            }};"""
        self.exec_script(js_val.format(name))
