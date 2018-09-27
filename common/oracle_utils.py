#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

# import os
import cx_Oracle

# 编码声明，解决乱码问题
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class OracleUtils(object):
    """
    Oracle数据库相关操作
    连接数据库名称如：db_name
    db_name = {"user": "数据库名称",
               "pwd": "数据库密码",
               "Database": "192.168.10.01:0000/ora11g"}
    """
    def __init__(self, db_name):
        self.db_info = db_name
        # 连接池方式
        self.conn = OracleUtil.__get_connect(self.db_info)

    @staticmethod
    def __get_connect(db_info):
        """
        静态方法，从连接池中取出连接
        :meth db_info:
        :return:
        """
        try:
            con = cx_Oracle.connect(db_info['user'], db_info['pwd'], db_info['dsn'])
            return con
        except Exception as err:
            print("数据库连接异常：{}".format(err))

    def get_rows(self, sql_data):
        """
        执行查询 sql
        :meth sql_data:
        :return:
        """
        try:
            cursor = self.conn.cursor()
            try:
                cursor.execute(sql_data)
                rows = cursor.fetchall()
                return rows
            except Exception as err:
                print("执行sql出现异常：{}".format(err))
            finally:
                cursor.close()
        except Exception as err:
            print("数据库连接异常：{}".format(err))

    def get_string(self, sql_data):
        """
        查询某个字段的对应值
        :meth sql_data:
        :return:
        """
        rows = self.get_rows(sql_data)
        if rows is not None:
            for row in rows:
                for i in row:
                    return i

    def execute_sql(self, sql_data):
        """
        执行 sql 语句
        :meth sql_data:
        :return:
        """
        try:
            cursor = self.conn.cursor()
            try:
                cursor.execute(sql_data)
            except Exception as err:
                print("执行sql出现异常：{}".format(err))
            finally:
                cursor.close()
        except Exception as err:
            print("数据库连接异常：{}".format(err))

    def close_conn(self):
        """
        关闭 orcle 连接
        :return:
        """
        try:
            self.conn.close()
        except Exception as err:
            print("数据库关闭时异常：{}".format(err))
