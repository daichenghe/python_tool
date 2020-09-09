
import hashlib
import serial
import MySQLdb
import time

print("please put com")
com_set = input()

serial = serial.Serial(com_set, 460800, timeout=0.1)
data = []
while len(data) == 0:
	#data = serial.read_all()
	data = serial.read(12)
for ele in data:
	pass
	
id_str = ''
for ele in data:
	ele_str = '%02x' % ele
	#print (ele_str)
	id_str+= ele_str
print(id_str)	
	
hl = hashlib.md5()
hl.update(data)
#print(data)

print(hl.hexdigest())
#print(len(hl.hexdigest()))

md5_from_rtk = hl.hexdigest()

print('md5_from_rtk = %s' % md5_from_rtk)
md5_buff = []
while len(md5_buff) == 0:
	time.sleep(1)
	print('wait')
	md5_buff = serial.read(16)
'''
for ele in md5_buff:
	print(ele)
'''

md5_str = ''
for ele in md5_buff:
	ele_str = '%02x' % ele
	#print (ele_str)
	md5_str+= ele_str
print("md5_str = %s" % md5_str)



def check_id(cursor,id):
	print(type(id))
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
		print('add')
		sql = "INSERT INTO openrtk_id(ID, \
		 USER_NAME, TYPE) \
		 VALUES ('%s', 'daich', 'ins') " % (id)
		print(sql)
		cursor.execute(sql)
	return is_use



if md5_str == md5_from_rtk:
	print('****************************************************')
	db = MySQLdb.connect("localhost", "root", "dch19901231", "openrtk", charset='utf8' )
	cursor = db.cursor()


	is_use = check_id(cursor,id_str)
	if is_use == True:
		print('used id')
	else:
		sql = "SELECT * FROM openrtk_user \
			   WHERE USER_NAME = %s" % ('\'daich\'')
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			MAX_NUM = row[2]
			BOARD_NUM = row[3]
			print('num = %d' % (BOARD_NUM))
			print('max_num = %d' % (MAX_NUM))
		if(BOARD_NUM < MAX_NUM):
			print('check suc')
			sql = "UPDATE openrtk_user SET CUR_NUM = %d WHERE USER_NAME = '%s'" % ((BOARD_NUM+1), ('daich'))
			cursor.execute(sql)
			db.commit()
			db.close()
		else:
			print('reached the max board number')