import sys
import os
import re
import serial.tools.list_ports
import subprocess
import shlex 
from base_class import uart_class as rts_uart

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

r, dev,com = rts_uart.detect_serials()
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
	if is_rtcm == "yes":
		subprocess.Popen(shlex.split(rtcm_cmd))
        if is_debug == 'yes':
		subprocess.Popen(shlex.split(debug_cmd))
	if is_user == "yes":
		subprocess.Popen(shlex.split(user_cmd))
	
