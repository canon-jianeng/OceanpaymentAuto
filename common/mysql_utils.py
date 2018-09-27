#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-15 09:00:00
# @Author  : Canon
# @Link    : https://www.python.org
# @Version : 3.6.1

import pymysql


class MysqlUtils(object):
    """
    mysql 数据库相关操作
    连接数据库信息：mysql_info
    mysql_info = {"host": '192.168.xx.xx',
                  "port": 3306,
                  "user": 'root',
                  "passwd": '11',
                  "db": 'xxx',
                  "charset": 'utf8'}
    """
    def __init__(self, mysql_info):
        self.db_info = mysql_info
        # 连接池方式
        self.conn = MysqlUtil.__get_connect(self.db_info)

    @staticmethod
    def __get_connect(db_info):
        """
        静态方法，从连接池中取出连接
        :meth db_info:
        :return:
        """
        try:
            conn = pymysql.connect(host=db_info['host'],
                                   port=db_info['port'],
                                   user=db_info['user'],
                                   passwd=db_info['passwd'],
                                   db=db_info['db'],
                                   charset=db_info['charset'])
            return conn
        except Exception as err:
            print("数据库连接异常：{}".format(err))

    def execute_sql(self, sql_data):
        """
        执行sql语句
        :meth sql_data:
        :return:
        """
        cur = self.conn.cursor()
        try:
            cur.execute(sql_data)
        except Exception as err:
            # sql执行异常后回滚
            self.conn.rollback()
            print("执行SQL语句出现异常：{}".format(err))
        else:
            cur.close()
            # sql无异常时提交
            self.conn.commit()

    def get_rows(self, sql_data):
        """
        返回查询结果
        :meth sql_data:
        :return:
        """
        cur = self.conn.cursor()
        try:
            cur.execute(sql_data)
        except Exception as err:
            print("执行SQL语句出现异常：{}".format(err))
        else:
            rows = cur.fetchall()
            cur.close()
            return rows

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

    def close_conn(self):
        """
        关闭 close mysql
        :return:
        """
        try:
            self.conn.close()
        except Exception as err:
            print("数据库关闭时异常：{}".format(err))
