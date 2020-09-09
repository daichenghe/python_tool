import os
import time
import datetime

def file_search(root_dir,signle_search):
    print ('start file search')
    for root,dirs,files in os.walk(root_dir):
        if signle_search == True:
            return dirs,files

def get_utc_day(time_list):
	'''
	year = int(time.strftime("%Y"))
	month = int(time.strftime("%m"))
	day = int(time.strftime("%d"))
	hour = int(time.strftime("%H"))
	minute = int(time.strftime("%M"))
	second = int(time.strftime("%S"))
	'''
	year = int(time_list[0])
	month = int(time_list[1])
	day = int(time_list[2])
	hour = int(time_list[3])
	minute = int(time_list[4])
	second = int(time_list[5])
	local_time = datetime.datetime(year, month, day, hour, minute, second)
	time_struct = time.mktime(local_time.timetuple())
	utc_st = datetime.datetime.utcfromtimestamp(time_struct)
	d1 = datetime.datetime(year, 1, 1)
	utc_sub = utc_st - d1
	utc_str = utc_sub.__str__()
	print(str(utc_st))
	utc_year_str = (str(utc_st))[0:4]
	utc_day_int = int(utc_str.split( )[0])
	utc_day_str = str(utc_day_int + 1)
	utc_hour_str = (str(utc_st))[5:7]
	return utc_day_str,utc_year_str,utc_hour_str