import serial
import binascii
import time
from time import sleep
import datetime


print "select com"
com_sel = raw_input()
com = '/dev/' + com_sel
print "1:ascii 2:hex" 
print "select"
#select = raw_input()
select = '1'
print "set log file"
#log_file = raw_input()
#localtime = time.localtime(time.time())
#print "time" ,localtime
time_now = datetime.datetime.now()
print time_now.year
log_file = str(time_now.year) + str(time_now.month) + str(time_now.day) + str(time_now.hour) + str(time_now.minute) + str(time_now.second)
fh = open(log_file,"wb")
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

if __name__ == '__main__':
	#serial = serial.Serial(com_set, 115200, timeout=0.5)  #/dev/ttyUSB0
	serial=serial.Serial(com,115200, timeout=1)
	if serial.isOpen() :
		print("open success")
	else :
		print("open failed")

	while True:
		data = recv(serial)
		#print(data)
		#print("receive : ",data)
		print(data)
                fh.write(data)
		#serial.write(data) 
