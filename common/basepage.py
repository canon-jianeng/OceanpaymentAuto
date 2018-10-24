#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

"""
# 拖动控件内的滚动条
# self.driver.execute_script("document.getElementsByClassName('dropdown-menu inner')[1].scrollTop=500;")
"""

import win32gui
import win32con
import time
import platform
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from common.logger import Log

# 日志
log = Log()


class Action(object):
    """
    BasePage封装所有页面的公共方法
    """
    def __init__(self, selenium_driver):
        """
        初始化 driver
        :param selenium_driver: 浏览器驱动
        """
        self.driver = selenium_driver

    def _open(self, url, page_title):
        """
        打开页面，校验页面链接是否加载正确
        :param url: 链接地址 type: str
        :param page_title: 页面标题 type: str
        :return:
        """
        # 使用 get 打开访问链接地址
        self.driver.get(url)
        try:
            # 使用 assert 进行校验, 打开的链接地址是否与配置的地址一致, 调用 on_page() 方法
            assert self.on_page(page_title), "打开页面失败 {}".format(url)
        except Exception as err:
            err_info = "打开页面失败 \n{}".format(err)
            raise Exception(err_info)

    def open(self, base_url, page_title):
        """
        定义 open 方法，调用 _open() 打开链接
        :return:
        """
        self._open(base_url, page_title)

    def on_page(self, page_title):
        """
        使用 current_url 获取当前窗口 url 地址，进行与配置地址作比较，返回比较结果（True or False）
        :param page_title: 页面标题 type: str
        :return: type: bool
        """
        return page_title in self.driver.title

    def find_element(self, time_out=10, *loc):
        """
        重写定位单个元素方法
        :param time_out: 超时时间 type: int
        :param loc: 元素定位 type: tuple
        :return:
        """
        try:
            # 等待元素出现
            # WebDriverWait(self.driver, 10).until(self.driver.find_element(*loc).is_displayed())
            WebDriverWait(self.driver, time_out).until(
                lambda driver: driver.find_element(*loc).is_displayed()
            )
            return self.driver.find_element(*loc)
        except Exception as err:
            err_info = "\n{} 页面未找到 {} 元素 \n页面链接:{} \n{}".format(
                self.driver.title, loc, self.driver.current_url, err
            )
            log.error(err_info)

    def find_all_elements(self, time_out=10, *loc):
        """
        定位多个元素方法
        :param time_out: 超时时间 type: int
        :param loc: 元素定位 type: tuple
        :return:
        """
        try:
            # 等待元素出现
            WebDriverWait(self.driver, time_out).until(
                lambda driver: driver.find_element(*loc)
            )
            return self.driver.find_elements(*loc)
        except Exception as err:
            err_info = "\n{} 页面未找到 {} 元素 \n页面链接:{} \n{}".format(
                self.driver.title, loc, self.driver.current_url, err
            )
            log.error(err_info)

    def switch_frame(self, type_str, ele_loc="", index=0):
        """
        切换 frame 标签
        :param type_str: 类型 type: str
            main: 切回主文档
            id: 用 id 来定位
            name: 用 name 来定位
            index: 用索引定位
            single: 单一对象,  用 WebElement 对象 (xpath) 来定位
            multi: 多个相同对象, 用  WebElement 对象 (xpath) 来定位
        :param tag_name: 元素定位 type: str
        :param index: 位置 type: int
        :return:
        """
        try:
            if type_str == "id" or type_str == "name":
                self.driver.switch_to.frame(ele_loc)
            elif type_str == "index":
                self.driver.switch_to.frame(index)
            elif type_str == "single":
                self.driver.switch_to.frame(self.driver.find_elements_by_xpath(ele_loc))
            elif type_str == "multi":
                self.driver.switch_to.frame(self.driver.find_elements_by_xpath(ele_loc)[index])
            elif type_str == "main":
                self.driver.switch_to.default_content()
        except Exception as err:
            err_info = "切换 frame 错误: {} \n{}".format(ele_loc, err)
            log.error(err_info)

    def exec_script(self, src):
        """
        用于执行js脚本，返回执行结果
        :param src: js 脚本 type: str
        :return:
        """
        try:
            return self.driver.execute_script(src)
        except Exception as err:
            err_info = "执行js脚本错误: {} \n{}".format(src, err)
            log.error(err_info)

    def send_keys(self, loc, value, flag=False, clear=True, *text_name):
        """
        重写 send_keys 方法
        :param loc: 元素定位 type: tuple
        :param value: 输入值 type: str
        :param text_name: 文本框名称 type: tuple
        :return:
        """
        try:
            if loc[0] == 'js':
                self.exec_script(loc[2])
            else:
                if flag is True:
                    # 点击文本框
                    self.find_element(int(loc[1]), *(loc[0], loc[2].format(text_name))).click()
                if clear is True:
                    # 清空文本框
                    self.find_element(int(loc[1]), *(loc[0], loc[2].format(text_name))).clear()
                # 输入文本值
                self.find_element(int(loc[1]), *(loc[0], loc[2].format(text_name))).send_keys(value)
        except Exception as err:
            err_info = "输入文本错误: {} \n{}".format(loc, err)
            log.error(err_info)

    def click_blank(self):
        # 点击空白区域
        ActionChains(self.driver).move_by_offset(0, 0).click().perform()

    def select_checkbox(self, loc):
        """
        勾选单个复选框
        :param loc: 元素定位 type: tuple
        :return:
        """
        try:
            if loc[0] == 'js':
                self.exec_script(loc[2])
            else:
                # 判断复选框是否被勾选
                if not self.find_element(int(loc[1]), *(loc[0], loc[2])).is_selected():
                    self.find_element(int(loc[1]), *(loc[0], loc[2])).click()
        except Exception as err:
            err_info = "勾选文本框错误: {} \n{}".format(loc, err)
            log.error(err_info)

    def mouse_move(self, loc):
        """
        模拟鼠标悬停
        :param loc: 元素定位 type: tuple
        :return:
        """
        try:
            # 鼠标移到悬停元素上
            ActionChains(self.driver).move_to_element(self.find_element(int(loc[1]), *(loc[0], loc[2]))).perform()
        except Exception as err:
            err_info = "鼠标悬停错误: {} \n{}".format(loc, err)
            log.error(err_info)

    def click_button(self, loc, *btn_name):
        """
        点击操作
        :param loc: 元素定位 type: tuple
        :param btn_name: 按钮名称 type: tuple
        :return:
        """
        try:
            if loc[0] == 'js':
                self.exec_script(loc[2])
            else:
                self.find_element(int(loc[1]), *(loc[0], loc[2].format(btn_name))).click()
        except Exception as err:
            err_info = "点击元素错误: {} \n{}".format(loc, err)
            log.error(err_info)

    def click_by_left(self, flag_loc, btn_loc, val):
        """
        根据左侧说明标识, 点击对应的元素
        :param flag_loc: 说明标识元素 type: tuple
        :param btn_loc: 点击元素 type: tuple
        :param val: 说明标识 type: str
        :return:
        """
        flag_list = self.find_all_elements(int(flag_loc[1]), flag_loc[0], flag_loc[2])
        for num in range(len(flag_list)):
            if flag_list[num].text.strip() == val.strip():
                self.find_element(int(btn_loc[1]), *(btn_loc[0], btn_loc[2].format(num))).click()
                break

    def click_by_name(self, btn_loc, val):
        """
        根据按钮名称点击按钮
        :param btn_loc: 按钮元素 type: tuple
        :param val: 按钮名称 type: str
        :return:
        """
        try:
            btn_list = self.find_all_elements(int(btn_loc[1]), btn_loc[0], btn_loc[2])
            for btn in btn_list:
                if btn.text.strip() == val.strip():
                    btn.click()
                    break
        except AttributeError as err:
            err_info = "点击元素错误: {} \n{}".format(btn_loc, err)
            log.error(err_info)

    def get_texts(self, title_loc, val_loc, index, title_val):
        """
        获取一组文本值对应的元素定位字典
        :param title_loc: 标题定位 type: tuple
        :param val_loc: 数据行定位 type: tuple
        :param index: 行数 type: int
        :param title_val: 标题值 type: int
        :return: text_dict
        """
        try:
            get_val = None
            text_list = self.find_all_elements(int(title_loc[1]), title_loc[0], title_loc[2])
            for num in range(len(text_list)):
                num_val = text_list[num].text.strip()
                if num_val == title_val:
                    new_path = val_loc[2].format(index, num + 1)
                    log.info("{}: {}".format(num_val, new_path))
                    get_val = self.get_text((val_loc[0], int(val_loc[1]), new_path))
                    break
            return get_val
        except Exception as err:
            err_info = "获取一组元素中的文本值错误: {}, {} \n{}".format(
                title_loc, val_loc, err
            )
            log.error(err_info)

    def exec_actions(self, title_loc, val_loc, title_val, action, val=""):
        """
        执行操作，输入、点击、选择
        :param title_loc: 左侧名称定位 type: tuple
        :param val_loc: 操作定位 type: tuple
        :param title_val: 左侧名称 type: str
        :param action: 操作，包括"click", "input", "select" type: str
        :param val: 输入值 type: str
        """
        try:
            text_list = self.find_all_elements(int(title_loc[1]), title_loc[0], title_loc[2])
            for num in range(len(text_list)):
                num_val = text_list[num].text.replace(":", "").replace("\n", "").strip()
                if num_val == title_val:
                    new_path = val_loc[2].format(num + 1)
                    log.info("{}: {}".format(num_val, new_path))
                    if action == "click":
                        self.click_button((val_loc[0], int(val_loc[1]), new_path))
                    elif action == "input":
                        self.send_keys((val_loc[0], int(val_loc[1]), new_path), val)
                    elif action == "select":
                        self.select_combobox((val_loc[0], int(val_loc[1]), new_path), val)
                    break
        except Exception as err:
            err_info = "获取一组元素中的文本值错误: {}, {} \n{}".format(
                title_loc, val_loc, err
            )
            log.error(err_info)

    def confirm_alert(self):
        # 模拟确认提示框
        try:
            val = self.driver.switch_to.alert.text
        except UnexpectedAlertPresentException:
            val = None
        except NoAlertPresentException:
            val = None
        if val:
            # (解决 UnexpectedAlertPresentException 异常)
            log.info(val)
            self.driver.switch_to.alert.accept()
        return val

    def select_combobox(self, loc, value, way="text"):
        """
        选择下拉框的值, <select>标签下拉菜单
        :param loc: 元素定位 type: tuple
        :param value: 选项值 type: str
        :param way: 选择方式 type: str
        :return:
        """
        try:
            if loc[0] == 'js':
                self.exec_script(loc[2])
            else:
                if way == "value":
                    # 通过 select 选项的 value 值来定位
                    Select(self.find_element(int(loc[1]), *(loc[0], loc[2]))).select_by_value(value)
                elif way == "index":
                    # 通过 select 选项的索引来定位
                    Select(self.find_element(int(loc[1]), *(loc[0], loc[2]))).select_by_index(value)
                elif way == "text":
                    # 通过 select 选项的文本内容来定位
                    Select(self.find_element(int(loc[1]), *(loc[0], loc[2]))).select_by_visible_text(value)
        except Exception as err:
            err_info = "选择下拉框错误: {} \n{}".format(loc, err)
            log.error(err_info)

    def select_ul(self, select_loc, item_loc, item):
        """
        选择下拉框的值, 非 "select" 标签的下拉菜单
        :param select_loc: 下拉框元素定位 type: tuple
        :param item_loc: 选项值元素定位 type: tuple
        :param item: 选项值 type: str
        :return:
        """
        try:
            self.click_button(select_loc)
            items_list = self.find_all_elements(int(item_loc[1]), item_loc[0], item_loc[2])
            # 判断这组元素对象中是否存在文本值为 item
            for ele_obj in items_list:
                if item.strip() == ele_obj.text.strip():
                    ele_obj.click()
                    break
        except Exception as err:
            err_info = "选择下拉框错误: {}, {} \n{}".format(
                select_loc, item_loc, err
            )
            log.error(err_info)

    def get_attrval(self, loc, value):
        """
        获取文本框的值
        :param loc: 元素定位 type: tuple
        :param value: 文本框的属性名 type: str
        :return:
        """
        try:
            if loc[0] == 'js':
                return self.exec_script(loc[2])
            else:
                return self.find_element(int(loc[1]), *(loc[0], loc[2])).get_attribute(value)
        except Exception as err:
            err_info = "获取文本框错误: {} \n{}".format(loc, err)
            log.error(err_info)

    def get_text(self, loc):
        """
        获取单个元素中的文本值
        :param loc: 元素定位 type: tuple
        :return:
        """
        try:
            if loc[0] == 'js':
                return self.exec_script(loc[2])
            else:
                return self.find_element(int(loc[1]), *(loc[0], loc[2])).text.strip()
        except Exception as err:
            err_info = "获取单个元素中的文本值错误: {} \n{}".format(loc, err)
            log.error(err_info)

    def is_exist(self, loc=()):
        # 若元素存在, 则返回元素文本值, 不存在, 则返回空
        try:
            WebDriverWait(self.driver, int(loc[1])).until(
                lambda driver: driver.find_element(*(loc[0], loc[2])).is_displayed()
            )
            return self.driver.find_element(*(loc[0], loc[2])).text.strip()
        except NoSuchElementException:
            return ""
        except TimeoutException:
            return ""

    def upload_file(self, loc, file_path):
        """
        上传文件
        :param loc: 元素定位 type: tuple
        :param file_path: 文件路径 type: str
        :return:
        """
        try:
            # 点击上传按钮
            self.click_button(loc)
            # 判断是哪个操作系统
            if platform.system() == "Windows":
                file_path = file_path.replace("/", "\\")
                log.info("上传文件路径:{}".format(file_path))
                # 主窗口(上传文件对话框), chrome 浏览器弹窗标题是"打开", firefox 浏览器弹窗标题是"文件上传"
                dialog = win32gui.FindWindow('#32770', '打开')
                # 重试次数
                num = 5
                for i in range(num):
                    # 判断是否获取到窗口句柄
                    if dialog == 0:
                        time.sleep(1)
                        dialog = win32gui.FindWindow('#32770', '打开')
                    else:
                        # 上面三句依次寻找对象，直到找到输入框 edit 对象的句柄
                        combobox_ex32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
                        combobox = win32gui.FindWindowEx(combobox_ex32, 0, 'ComboBox', None)
                        edit = win32gui.FindWindowEx(combobox, 0, 'Edit', None)
                        # 确定按钮
                        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
                        # 在输入框中, 输入绝对路径
                        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
                        # 点击打开按钮
                        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
                        break
                if dialog == 0:
                    err_info = "上传文件失败\n 上传按钮定位: {}\n 上传文件: {}\n ".format(loc, file_path)
                    log.error(err_info)
        except Exception as err:
            err_info = "上传文件失败: {} {}\n{}".format(loc, file_path, err)
            log.error(err_info)
