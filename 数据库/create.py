# -*- coding:utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(host='localhost', user='root', passwd='dch19901231')
cursor=conn.cursor()
cursor.execute("""create database if not exists db_pytest""")
conn.select_db('db_pytest')
cursor.execute("create table tb_test(id int, info varchar(100))")
cursor.close()

print ('hello')

'''
import pymysql

# 打开数据库
db = pymysql.connect(host='localhost',port =3306,user='root',passwd='dch19901231',db='sys',charset='utf8' )

#使用cursor()方法获取操作游标
cursor = db.cursor()

#如果数据表已经存在使用execute()方法删除表
cursor.execute("drop table if EXISTS income")

#创建数据库SQL语句
#time,ironincome,general_income,baiincome
SQL = """CREATE TABLE `income` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datetime` varchar(20) DEFAULT NULL,
  `ironincome` decimal(20,2) DEFAULT NULL,
  `generalincome` decimal(20,2) DEFAULT NULL,
  `baiincome` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""
cursor.execute(SQL)

db.close()
'''