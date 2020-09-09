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
import _thread





def file_search(root_dir,signle_search):
    print ('start file search')
    for root,dirs,files in os.walk(root_dir):
        if signle_search == True:
            return dirs


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

def log_data(com,baud,timeout,is_log,file_name):
	serial = rts_uart.uart_communicate(com,baud,timeout,is_log,file_name)
	if (serial.is_connect):
		serial.recive_data(1)
		serial.log_file_close()


rtk_index = 0
get_new_rtk_flag = False
old_search = -1
mount_path = file_search('/media/pi/',True)
while True: 
	time.sleep(2)
	print('search')
	r, dev,com = rts_uart.detect_serials()
	com_set_num = -1
	dev_uart_list = ['user','st','debug','rtcm']
	log_file_list = []
	print('old_search = %s' % old_search)
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
			#com = ['/dev/ttyUSB' + str(x) for x in com]	#linux
			com_str = ['com' + str(x) for x in com]		#windows
			print ("find rtk serial start %s" % com_str[com_set_num])
			file_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
			day = get_utc_day()
			mkpath='./' + day
			mkdir(mkpath)
			for k in range(4):												#??????
				log_file_list.append(mkpath + '/' + dev_uart_list[k] + '_' + file_time + '.bin')
			    #_thread.start_new_thread( print_time, ("Thread-1", 2, ) )
				_thread.start_new_thread(log_data, ((com_str[com_set_num + k],460800,0.5,True,log_file_list[k])))
				#t = threading.Thread(target=log_data(com_str[com_set_num + k],460800,0.5,True,log_file_list[k]))
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

