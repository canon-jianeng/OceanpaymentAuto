#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import xlrd


class ExcelUtils(object):
    def __init__(self, excel_path, sheet_name):
        # 打开 excel 文件
        self.data = xlrd.open_workbook(excel_path)
        # 获取指定的 sheet
        self.sheet = self.data.sheet_by_name(sheet_name)
        # 获取第一行的值
        self.row = self.sheet.row_values(0)
        # 获取第一列的值
        self.col = self.sheet.col_values(0)
        # excel 表的行数
        self.rowNum = self.sheet.nrows
        # excel 表的列数
        self.colNum = self.sheet.ncols
        # 当前行号
        self.curRowNo = 1

    def has_next(self):
        """
        当行数为0或者读取的行数小于行号时, 返回 False
        :return: True or False type: bool
        """
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

    def list_in_dict(self):
        """
        生成包含字典的列表数据, 第二行数据作为字典的键, 第三行及之后的数据作为字典的值
        返回形式: [{}, {}, {}]
        :return: data_list type: list
        """
        data_list = []
        row_val = self.sheet.row_values(1)
        self.curRowNo += 1
        while self.has_next():
            data_dict = {}
            col = self.sheet.row_values(self.curRowNo)
            for x in range(self.colNum):
                if row_val[x] == "Skip" and col[x] == "Yes":
                    break
                else:
                    data_dict.setdefault(row_val[x], col[x])
            data_list.append(data_dict)
            self.curRowNo += 1
        return data_list

    def read_merged(self):
        """
        按行读取, 去除头尾空字符
        第一行数据为两个合并单元格，'TestData', 'TestResult'
        第二行数据作为字典的键, 第三行及之后的数据作为字典的值
        返回形式: [{'TestData' :{}, 'TestResult': {}},
                   {'TestData' :{}, 'TestResult': {}} ...]
        :return: data_list type: list
        """
        merged_data = []
        skip_title = self.sheet.cell_value(1, 0).strip()
        # 合并单元格为一个元组的集合，每个元组由4个数字构成
        # (行开始, 行结束, 列开始, 列结束), 不包含结束位置
        if self.sheet.merged_cells:
            skip_num = 0
            for row in range(self.rowNum):
                # 获取多个合并单元格的数据
                for count in range(len(self.sheet.merged_cells)):
                    item = self.sheet.merged_cells[count]
                    # 合并单元格的第一个单元格的值
                    key_val = self.sheet.cell_value(item[0], item[2]).strip()
                    item_dict = {}
                    row_dict = {}
                    # 合并单元格的列数
                    col_num = range(item[2], item[3])
                    for col in col_num:
                        skip_val = self.sheet.cell_value(row, 0).strip()
                        if row > 1 and skip_title == "Skip":
                            if skip_val == "Yes":
                                break
                            else:
                                row_dict.setdefault(
                                    self.sheet.cell_value(1, col).strip(),
                                    self.sheet.cell_value(row, col).strip()
                                )
                            # 当列数等于合并单元格最后一个单元格的列数, 生成字典
                            if col == item[3]-1:
                                # 合并单元格的第一个单元格, 添加到列表
                                if count == 0:
                                    item_dict[key_val] = row_dict
                                    merged_data.append(item_dict)
                                    skip_num += 1
                                # 第三行开始获取数据
                                merged_data[skip_num-1][key_val] = row_dict
        return merged_data

    def row_list(self, row_num):
        """
        按行读取, 去除空字符
        :meth row_num: 行号 type: str
        :return: data_list type: list
        """
        data_list = self.sheet.row_values(row_num)
        n = data_list.count("")
        for i in range(n):
            data_list.remove('')
        return data_list

    def read_as_dict(self):
        """
        按行读取, 第一列作为键, 生成字典数据
        :return: data_dict type: dict
        """
        data_dict = {}
        col = self.sheet.col_values(0)
        n_rows = self.sheet.nrows
        for i in range(n_rows):
            val = self.row_list(i)[1:]
            if len(val) == 1:
                data_dict.setdefault(col[i], val[0])
            else:
                data_dict.setdefault(col[i], val)
        return data_dict


if __name__ == '__main__':
    value = ExcelUtils("../data/testdata/gateway/ThreePay.xlsx", "PayPage").read_merged()
    print(value)
