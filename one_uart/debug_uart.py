import serial
import binascii
import time
from time import sleep
import datetime
import json
import os
import sys

file_init_flag = 0


com_sel = 'ttyUSB2'
com = ''
#com = '/dev/' + com_sel
if len(sys.argv) > 1:
	com = str(sys.argv[1])
else:
	print ("select com")
	com = input()
print (com)
select = '1'
time_now = datetime.datetime.now()
print (time_now.year)

json_cmd = [ {"username":"ymj_123","apikey":"SIGEMZOOMQ1JDJI3","ntripType":"LocalNTRIP","rtkType":"LocalRTK",\
"url":[106, 12, 40, 121],"port":2201,"mountPoint":"/RTK","otherNtripUsername":"abc","otherNtripApikey":"123456"} ]

def recv(serial):
	while True:
		if select == "1":
			data = serial.read_all()
			#print('get data')
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
	#return utc_st


def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        print (path+' mkdir suc')
        return True
    else:
        print ('mkdir exist')
        return False



file_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
#mk_time =   time.strftime("%Y_%m_%d",time.localtime())
day = get_utc_day()
mkpath='./' + day
mkdir(mkpath)
log_file = mkpath + '/' + 'debug_' + file_time
print (log_file)
if __name__ == '__main__':
	fh = open(log_file,"wb")
	#serial = serial.Serial(com_set, 115200, timeout=0.5)  #/dev/ttyUSB0
	serial=serial.Serial(com,460800, timeout=1)
	#serial.write(json)
	print (json)
	if serial.isOpen() :
		print("open success")
	else :
		print("open failed")

	while True:
		data = recv(serial)
		fh.write(data)
