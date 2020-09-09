import MySQLdb




def check_id(cursor,id):
	sql = "SELECT * FROM openrtk_id \
		   WHERE ID > %s" % (0)
	cursor.execute(sql)
	results = cursor.fetchall()
	print(results)
	is_use = False
	for row in results:
		if row[0] == id:
			print('have checked')
			is_use = True
			break;
	if is_use == True:
		pass
	else:
		sql = "INSERT INTO openrtk_id(ID, \
		 USER_NAME, TYPE) \
		 VALUES (%s, 'daich', 'ins') " % (id)
		print(sql)
		cursor.execute(sql)

db = MySQLdb.connect("localhost", "root", "dch19901231", "openrtk", charset='utf8' )
cursor = db.cursor()

check_id(cursor,'123456')
'''
sql = "SELECT * FROM access_control \
       WHERE USER_NAME = %s" % ('\'daich\'')
print(sql)
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
	BOARD_NUM = row[2]
	print('num = %d' % (BOARD_NUM))

sql = "UPDATE access_control SET BOARD_NUM = %d WHERE USER_NAME = '%s'" % ((BOARD_NUM+1), ('daich'))
print(sql)
cursor.execute(sql)
'''
db.commit()
db.close()