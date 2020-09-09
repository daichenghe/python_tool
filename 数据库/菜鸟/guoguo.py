#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "dch19901231", "TESTDB", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS QIANQIANGUO")
#cursor.execute("create table tb_test(id int, info varchar(100))")
# 创建数据表SQL语句
sql = """CREATE TABLE QIANQIANGUO (
         NAME  CHAR(20) NOT NULL,
         IDENTIYR   CHAR(20),
         BRITHDAY CHAR(50) )"""

cursor.execute(sql)


sql = """INSERT INTO QIANQIANGUO(NAME,
         IDENTIYR, BRITHDAY)
         VALUES ('qianqian', 'mother', '1990-09-13')"""
cursor.execute(sql)
db.commit()

sql = """INSERT INTO QIANQIANGUO(NAME,
         IDENTIYR, BRITHDAY)
         VALUES ('guoguo', 'son', '2017-12-01')"""
cursor.execute(sql)
db.commit()

sql = """INSERT INTO QIANQIANGUO(NAME,
         IDENTIYR, BRITHDAY)
         VALUES ('dch', 'father', '1991-02-05')"""
cursor.execute(sql)
db.commit()

# 关闭数据库连接
db.close()