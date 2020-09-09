import sys
import os
import re
import serial.tools.list_ports
import subprocess
import shlex 
import copy
import time
import datetime
from base_class import uart_class as rts_uart
from base_class import tool_class as tools
import _thread


def log_data(com,baud,timeout,is_log,file_name):
	try:
		serial = rts_uart.uart_communicate(com,baud,timeout,is_log,file_name)
		#print(com)
		#print(is_log)
		#print(file_name)
		if (serial.is_connect):
			serial.recive_data(1)
			serial.log_file_close()
	except:
		print ('end')

mount_path = tools.file_search('/media/pi/',True)
print (mount_path)
if mount_path:
    mount_path_str = os.path.join('/media/pi/',mount_path[0])
else:
    mount_path_str = './'
day = tools.get_utc_day()
mkpath = os.path.join(mount_path_str,day)
tools.mkdir(mkpath)

file_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
#log_file = mkpath + '/' + 'ublox_' + file_time
log_file = mkpath + '/' + 'ublox_' + file_time +'.bin'
print (log_file)
r, dev,com_num = rts_uart.detect_serials()
#print ("r = %s" % r)
#print ("dev = %s" % dev)
#print ("com_num = %s" % com_num)
com_select = dev[0]
print(com_select)

if __name__ == '__main__':
	log_data(com_select,460800,0.5,True,log_file)
