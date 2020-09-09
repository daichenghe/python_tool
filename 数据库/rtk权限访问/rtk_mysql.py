import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='dch19901231')
cursor=conn.cursor()
cursor.execute("""create database if not exists openrtk""")
conn.select_db('openrtk')
#cursor.execute("create table access_control(id int, info varchar(100))")
sql = """CREATE TABLE ACCESS_CONTROL (
         USER_NAME  CHAR(20) NOT NULL,
         USER_KEY   CHAR(20),
         BOARD_NUM  INT,
         ATTRIBUTE  CHAR(10),
         ACCESS CHAR(50) )"""
cursor.execute(sql)
cursor.close()

print ('hello')