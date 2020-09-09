import sys
import os
import re
import serial.tools.list_ports
import subprocess
import shlex 

def print_serial(port):
	print("---------------[ %s ]---------------" % (port.name))
	print("Path: %s" % (port.device))
	print("Descript: %s" % (port.description))
	print("HWID: %s" % (port.hwid))
	if not None == port.manufacturer:
		print("Manufacture: %s" % (port.manufacturer))
	if not None == port.product:
		print("Product: %s" % (port.product))
	if not None == port.interface:
		print("Interface: %s" % (port.interface))
	print()

 

def detect_serials():
	print "start search serials"
	ports = serial.tools.list_ports.comports()
	port_cnt = 0
	port_list = []
	port_num = []
        #print(ports)
	for port in ports:
            #print (port)
            #result = 'U' in str(port)
            #print result
            if (('USB' in str(port)) == True):
                print('find')
		port_str = str(port.device)
		port_num.append(int(port_str[11:]))
		port_list.append(port)
		port_num.sort();
                print (port)
	return (port_cnt, port_list,port_num)

 
 

r, dev,com = detect_serials()
'''
for com_num in com:
	if (com_num+1 in com) and (com_num+2 in com) and (com_num+3 in com):
		print com_num
'''
com_set_num = -1
for i in range(len(com)):
	if (com[i]+1 in com) and (com[i]+2 in com) and (com[i]+3 in com):
		com_set_num = i
		#print com_set_num
		break
com_str = []
com = ['/dev/ttyUSB' + str(x) for x in com]
print "find rtk serial start %s" % com[com_set_num]
if(com_set_num > -1):
	print "start"
	
	user_cmd = "python user_uart.py " + com[com_set_num]
	debug_cmd = "python debug_uart.py " + com[com_set_num + 2]
	rtcm_cmd = "python rtcm_uart.py " + com[com_set_num + 3]
	'''
	user_cmd = "python ./user_uart.py " + 'com18'
	debug_cmd = "python ./debug_uart.py " + 'com20'
	rtcm_cmd = "python ./rtcm_uart.py " + 'com21'
	'''
	while True:
		print "save user data? yes or no"
		is_user = raw_input()
		if (is_user == "yes") or (is_user == "no"):
			break
		else:
			print "not right cmd,please try again!"
	while True:
		print "save debug data? yes or no"	
		is_debug = raw_input()
		if (is_debug == "yes") or (is_debug == "no"):
			break
		else:
			print "not right cmd,please try again!"
	while True:
		print "save rtcm data? yes or no"	
		is_rtcm = raw_input()
		if (is_rtcm == "yes") or (is_rtcm == "no"):
			break
		else:
			print "not right cmd,please try again!"
	#os.system
	if is_rtcm == "yes":
		subprocess.Popen(shlex.split(rtcm_cmd))
                #subprocess.Popen(shlex.split('python ./user_uart.py /dev/ttyUSB0'))
                #os.system('python ./user_uart.py /dev/ttyUSB0')
        if is_debug == 'yes':
		subprocess.Popen(shlex.split(debug_cmd))
                #subprocess.Popen('python ./debug_uart.py /dev/ttyUSB2')
                #os.system('python ./debug_uart.py /dev/ttyUSB2')
	if is_user == "yes":
		subprocess.Popen(shlex.split(user_cmd))
	
