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
import platform

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
		print('end')


rtk_index = 0
get_new_rtk_flag = False
old_search = -1
mount_path = tools.file_search('/media/pi/',True)
print (mount_path)
if mount_path:
    mount_path_str = os.path.join('/media/pi/',mount_path[0])
else:
    mount_path_str = './'
    
print (mount_path)


if __name__ == '__main__':
	while True: 
		time.sleep(2)
		print('search')
		r, dev,com = rts_uart.detect_serials()
		com_set_num = -1
		dev_uart_list = ['user','st','debug','rtcm']
		log_file_list = []
		print('old_search = %s, com = %s' % (old_search,com))
		if(com[-1] > old_search):
			for i in range(rtk_index,len(com)):
				if (com[i]+1 in com) and (com[i]+2 in com) and (com[i]+3 in com):
					com_set_num = i     
					print('com_set_num = %d' % com_set_num)
					print('com_set_list = %d' % com[com_set_num])
					#rtk_index += 4
					rtk_index +=  4
					old_search = rtk_index
					print('old_search = %s' % old_search)
					get_new_rtk_flag = True
					break
			if(com_set_num > -1) and get_new_rtk_flag == True:
				work_os = platform.system()
				if (work_os == 'Linux'):
					com_str = ['/dev/ttyUSB' + str(x) for x in com]	#linux
				elif (work_os == 'Windows'):
					com_str = ['com' + str(x) for x in com]		#windows		
				print (com_str)					
				print ("find rtk serial start %s" % com_str[com_set_num])
				file_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
				day = tools.get_utc_day()
				#mkpath='./' + day
				mkpath = os.path.join(mount_path_str,day)
				tools.mkdir(mkpath)
				for k in range(4):												#??????
					log_file_list.append(mkpath + '/' + dev_uart_list[k] + '_' + file_time + '.bin')
					_thread.start_new_thread(log_data, ((com_str[com_set_num + k],460800,0.5,True,log_file_list[k])))
					#t.start() 
				print (log_file_list)
			'''
			if(com_set_num > -1) and get_new_rtk_flag == True:
				print "start"
				get_new_rtk_flag = False
				user_cmd = "python user_uart.py " + com[com_set_num]
				debug_cmd = "python debug_uart.py " + com[com_set_num + 2]
				rtcm_cmd = "python rtcm_uart.py " + com[com_set_num + 3]
				is_rtcm = 'yes'
				is_debug = 'yes'
				is_user = 'yes'
				#os.system
				if is_rtcm == "yes":
					subprocess.Popen(shlex.split(rtcm_cmd))
				if is_debug == 'yes':
					subprocess.Popen(shlex.split(debug_cmd))
				if is_user == "yes":
					subprocess.Popen(shlex.split(user_cmd))
				'''

