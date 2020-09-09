#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "dch19901231", "openrtk", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO access_control(
         USER_NAME, USER_KEY, BOARD_NUM, ATTRIBUTE,ACCESS)
         VALUES ('daich', '123456', 20, 'ins', 'vip')"""
		
cursor.execute(sql)
# 提交到数据库执行
db.commit()

'''
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   print('1111111111')
   db.rollback()
'''
# 关闭数据库连接
db.close()