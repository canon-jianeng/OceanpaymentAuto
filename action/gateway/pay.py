#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import pageobj.gateway.pay_page as Pay
from common.logger import Log


class PayAction(object):
    def __init__(self, driver):
        self.driver = driver
        self.log = Log()

    def put_pay(self, test_data):
        # 提交支付
        pay_page = Pay.Pay(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        if '/web/vpay' in self.driver.current_url:
            # 切换 frame
            pay_page.loc_frame()
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        pay_page.input_card_number(num)
        self.log.info("选择年月")
        pay_page.select_card_month()
        pay_page.select_card_year()
        self.log.info("输入 Secure Code")
        pay_page.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        pay_page.click_pay_now()

    def put_starcor(self, test_data):
        # 提交支付
        starcor = Pay.Starcor(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        starcor.input_card_number(num)
        self.log.info("输入年月")
        starcor.input_card_month()
        starcor.input_card_year()
        self.log.info("输入 Secure Code")
        starcor.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        starcor.click_pay_now()

    def put_standard(self, test_data):
        # 提交支付
        billing_pay = Pay.Standard(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        billing_pay.input_card_number(num)
        self.log.info("选择年月")
        billing_pay.select_card_month()
        billing_pay.select_card_year()
        self.log.info("输入 Secure Code")
        billing_pay.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        billing_pay.click_pay_now()

    def put_ncgame(self, test_data):
        # 提交支付
        ncgame_pay = Pay.Ncgame(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        # 切换 frame
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[1])
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        ncgame_pay.input_card_number(num)
        self.log.info("选择年月")
        ncgame_pay.select_card_month()
        ncgame_pay.select_card_year()
        self.log.info("输入 Secure Code")
        ncgame_pay.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        ncgame_pay.click_continue()

    def put_safe(self, test_data):
        # 提交支付
        safe_pay = Pay.Safe(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        safe_pay.input_card_number(num)
        self.log.info("选择年月")
        safe_pay.select_card_month()
        safe_pay.select_card_year()
        self.log.info("输入 Secure Code")
        safe_pay.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        safe_pay.click_pay_now()

    def put_inst(self, test_data):
        # 提交支付
        installment = Pay.Inst(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        self.log.info("输入 CPF/CNPJ")
        installment.input_cpf(test_data['CPF/CNPJ'])
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        installment.input_card_number(num)
        self.log.info("选择年月")
        installment.select_card_month()
        installment.select_card_year()
        self.log.info("输入 Secure Code")
        installment.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        installment.click_pay_now()

    def put_multiple(self, test_data):
        # 提交支付
        multiplepay = Pay.Multiple(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        self.log.info("点击 VISA 图片")
        multiplepay.click_visa()
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        multiplepay.input_card_number(num)
        self.log.info("选择年月")
        multiplepay.select_card_month()
        multiplepay.select_card_year()
        self.log.info("输入 Secure Code")
        multiplepay.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        multiplepay.click_continue()

    def put_quick(self, test_data):
        # 提交支付
        quick_pay = Pay.Quick(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        quick_pay.input_card_number(num)
        self.log.info("选择年月")
        quick_pay.input_card_month()
        quick_pay.input_card_year()
        self.log.info("输入 Secure Code")
        quick_pay.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        quick_pay.click_pay_now()

    def put_ever(self, test_data):
        # 提交支付
        evermarker_pay = Pay.Ever(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        evermarker_pay.input_card_number(num)
        self.log.info("输入年月")
        evermarker_pay.input_expiration()
        self.log.info("输入 Secure Code")
        evermarker_pay.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        evermarker_pay.click_confirm()

    def put_secure(self, test_data):
        # 提交支付
        pblsecure_pay = Pay.Secure(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        self.log.info("点击 '同意' 按钮")
        pblsecure_pay.click_agree()
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        pblsecure_pay.input_card_number(num)
        self.log.info("输入年月")
        pblsecure_pay.input_expiration()
        self.log.info("输入 Secure Code")
        pblsecure_pay.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        pblsecure_pay.click_pay_now()

    def put_web(self, test_data):
        # 提交支付
        web_pay = Pay.Web(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        web_pay.input_card_number(num)
        self.log.info("输入年月")
        web_pay.input_expiration()
        self.log.info("输入 Secure Code")
        web_pay.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        web_pay.click_pay_now()

    def put_virtual(self, test_data):
        # 提交支付
        virtual_pay = Pay.Virtual(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        # 切换 frame
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("iframe")[1])
        self.log.info("输入 CPF/CNPJ")
        virtual_pay.input_cpf(test_data['CPF/CNPJ'])
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        virtual_pay.input_card_number(num)
        self.log.info("选择年月")
        virtual_pay.select_card_month()
        virtual_pay.select_card_year()
        self.log.info("输入 Secure Code")
        virtual_pay.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 Continue")
        virtual_pay.click_continue()

    def put_webbr(self, test_data):
        # 提交支付
        web_brpay = Pay.WebBr(self.driver)
        self.log.info("----- 页面链接: %s -----" % self.driver.current_url)
        self.log.info("输入 CPF/CNPJ")
        web_brpay.input_cpf(test_data['CPF/CNPJ'])
        num = test_data['CardNumber']
        self.log.info("输入 Card Number: {}".format(num))
        web_brpay.input_card_number(num)
        self.log.info("输入年月")
        web_brpay.input_expiration()
        self.log.info("输入 Secure Code")
        web_brpay.input_secure_code(test_data['SecureCode'])
        self.log.info("点击 PAY NOW")
        web_brpay.click_pay_now()
