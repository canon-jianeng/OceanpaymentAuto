#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import xml.etree.ElementTree as Et


class XmlUtils(object):
    def __init__(self, xml_path):
        # 打开xml文档
        self.tree = Et.ElementTree(file=xml_path)
        # 获得根元素对象
        self.root_obj = self.tree.getroot()

    def get_tag(self):
        """
        获得根节点名称
        :return: type: str
        """
        return self.root_obj.tag

    def get_attribute(self):
        """
        获得根节点属性
        :return: type: str
        """
        return self.root_obj.attrib

    def get_val_by_tag(self, tag, tag_val, *attrib_name):
        """
        根据标签名和标签值获取某一属性值
        :meth tag: 标签名称 type: str
        :meth tag_val: 标签值 type: str
        :meth attrib_name: 属性名称 type: tuple
        :return: attrib_name 对应的属性值 type: tuple
        """
        data_list = []
        # 遍历某一个标签的全部数据
        for sub_item in self.root_obj.iter(tag):
            if sub_item.text == tag_val:
                for i in attrib_name:
                    data_list.append(sub_item.attrib[i])
        return tuple(data_list)

    def get_attr_by_tag(self, sec_attr, sec_value, third_tag):
        """
        根据二级标签的 sec_name 遍历此标签下的标签名为 third_tag 的所有属性数据
        :meth sec_attr: 二级标签的属性名 type: str
        :meth sec_value: sec_attr 对应的属性值 type: str
        :meth third_tag: 三级标签的标签名 type: str
        :return: third_tag 对应的所有属性数据 type: dict
        """
        data_dict = {}
        # 遍历 root 的下一层
        for next_node in self.root_obj:
            # 遍历 third_tag 标签的所有数据
            if next_node.attrib[sec_attr] == sec_value:
                for sub_item in next_node.iter(third_tag):
                    data_dict.setdefault(sub_item.text, tuple(sub_item.attrib.values()))
        return data_dict

    def get_dict_by_tag(self, tag, attr):
        """
        通过标签和其属性值获取下一级标签的所有属性数据
        :meth tag: 标签 type: str
        :meth attr: tag 的属性 type: str
        :return: tag 的下一级标签的所有属性数据 type: dict
        """
        sec_dict = {}
        for sub_tag in self.tree.findall(tag):
            data_dict = {}
            for sub_item in sub_tag.findall("locator"):
                data_dict.setdefault(sub_item.text, sub_item.attrib)
            sec_dict.setdefault(sub_tag.get(attr), data_dict)
        return sec_dict


if __name__ == '__main__':
    print(XmlUtils('../data/locator/gateway/PayPage.xml').get_attr_by_tag("pageName", 'webpay', 'locator'))
