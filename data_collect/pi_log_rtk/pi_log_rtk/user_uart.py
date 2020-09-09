import serial
import binascii
import time
from time import sleep
import datetime
import os
import sys


#print ('num:', str(sys.argv[1]))
#print "select com"
#com_sel = raw_input()
file_init_flag = 0
#com_sel = str(sys.argv[1])
#com = '/dev/' + com_sel
#com = str(sys.argv[1])
if len(sys.argv) > 1:
	com = str(sys.argv[1])
else:
	print "select com"
	com = raw_input()
#print com
#print "1:ascii 2:hex" 
#print "select"
#select = raw_input()
select = '1'
#print "set log file"
#log_file = raw_input()
#localtime = time.localtime(time.time())
#print "time" ,localtime
time_now = datetime.datetime.now()
print time_now.year
'''
log_file = 'user_' + str(time_now.year) + str(time_now.month) + str(time_now.day) + '_' + str(time_now.hour) + '_' +  str(time_now.minute) + '_' + str(time_now.second)
fh = open(log_file,"wb")
'''
def recv(serial):
	while True:
		if select == "1":
			data = serial.read_all()
			#data = "test"
		else:
			data = binascii.b2a_hex(serial.read_all())
		if data == '':
			continue
		else:
			break
		#sleep(0.02)
	return data

def get_utc_day():
	year = int(time.strftime("%Y"))
	month = int(time.strftime("%m"))
	day = int(time.strftime("%d"))
	hour = int(time.strftime("%H"))
	minute = int(time.strftime("%M"))
	second = int(time.strftime("%S"))
	local_time = datetime.datetime(year, month, day, hour, minute, second)
	time_struct = time.mktime(local_time.timetuple())
	utc_st = datetime.datetime.utcfromtimestamp(time_struct)
	
	d1 = datetime.datetime(year, 1, 1)
	utc_sub = utc_st - d1
	utc_str = utc_sub.__str__()
	utc_day_int = int(utc_str.split( )[0])
	utc_day_str = str(utc_day_int + 1)
	return utc_day_str

def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        print path+' mkdir suc'
        return True
    else:
        print 'mkdir exist'
        return False

file_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
#mk_time =   time.strftime("%Y_%m_%d",time.localtime())
#mkpath='./' + mk_time
day = get_utc_day()
mkpath='./' + day
mkdir(mkpath)
log_file = mkpath + '/' + 'user_' + file_time + '.bin'
print log_file

if __name__ == '__main__':
	#serial = serial.Serial(com_set, 115200, timeout=0.5)  #/dev/ttyUSB0
	serial=serial.Serial(com,460800, timeout=1)
	if serial.isOpen() :
		print("open success")
	else :
		print("open failed")

	while True:
		data = recv(serial)
		#print(data)
		#print("receive : ",data)
		if data != '' and file_init_flag == 0:
			fh = open(log_file,"wb")
			file_init_flag = 1
		if file_init_flag == 1:
			fh.write(data)
		#serial.write(data) 
