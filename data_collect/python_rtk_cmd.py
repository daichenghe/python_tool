import serial
import binascii
import time
from time import sleep
import datetime
import json

print "select com"
#com_sel = raw_input()
com_sel = 'ttyUSB2'
com = 'com20'
print "1:ascii 2:hex" 
print "select"
#select = raw_input()
select = '1'
print "set log file"

time_now = datetime.datetime.now()
print time_now.year
'''
cmd_json = '{"username":"ymj_123","apikey":"SIGEMZOOMQ1JDJI3","ntripType":"LocalNTRIP","rtkType":"LocalRTK",\
"url":[106, 12, 40, 121],"port":2201,"mountPoint":"/RTK","otherNtripUsername":"abc","otherNtripApikey":"123456"} '
'''

json_cmd = [ {"username":"ymj_123","apikey":"SIGEMZOOMQ1JDJI3","ntripType":"LocalNTRIP","rtkType":"LocalRTK",\
"url":[106, 12, 40, 121],"port":2201,"mountPoint":"/RTK","otherNtripUsername":"abc","otherNtripApikey":"123456"} ]
print "set url"
url = raw_input()
json_cmd[0]['port'] = int(url)
json = json.dumps(json_cmd)
print json
fh = open("test.txt",'w')
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
	serial=serial.Serial(com,460800, timeout=1)
	if serial.isOpen() :
		print("open success")

		serial.write(cmd_json)
	else :
		print("open failed")

	while True:
		data = recv(serial)
		#print(data)
		#print("receive : ",data)
		print(data)
		#serial.write(data) 
