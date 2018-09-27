#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

from common import basepage


class ResultObj(basepage.Action):
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)

    def return_val(self, tag_val):
        js_val = """
          function getval(tag_name){
            var arr = document.getElementsByTagName('td');
            for(var i=0; i<arr.length; i=i+2){
              if (arr[i].textContent.trim().replace(":", "") == tag_name){
                if (arr[i+1].children.length == 0){
                  return arr[i+1].textContent.trim();
                }else{
                  return arr[i+1].children[0].value.trim();
                };
              };
            };
          };
        """
        run_val = "return getval('{}');"
        exec_js = js_val + run_val.format(tag_val)
        if tag_val == "":
            return ""
        else:
            return self.exec_script(exec_js)

    def return_tagval(self, tag_name):
        js_val = """
          function returnval(tag_name){
            var val=document.getElementsByTagName(tag_name);
            return val[val.length-1].textContent;
          };
        """
        run_val = "return returnval('{}');"
        exec_js = js_val + run_val.format(tag_name)
        if tag_name == "":
            return ""
        else:
            return self.exec_script(exec_js)

    def return_check(self, tag_name):
        js_val = """
                  function returnval(tag_name){
                    var val=document.firstElementChild.getElementsByTagName(tag_name);
                    return val[val.length-1].textContent;
                  };
                """
        run_val = "return returnval('{}');"
        exec_js = js_val + run_val.format(tag_name)
        if tag_name == "":
            return ""
        else:
            return self.exec_script(exec_js)
