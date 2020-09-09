#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 17:28
# @Author  : zengsk in HoHai

import os
import sys
from ftplib import FTP
import gzip
import time
import datetime

def un_gz(file_name):
	print("un_gz")
	file_now = './data/' + file_name
	f_name = file_now.replace(".gz", "")
	g_file = gzip.GzipFile(file_now)
	open(f_name, "wb+").write(g_file.read())
	g_file.close()


# 连接ftp服务器
def ftpConnect(ftpserver, port, usrname, password):
    ftp = FTP()
    try:
        ftp.connect(ftpserver, port)
        ftp.login(usrname, password)
    except:
        raise IOError(' FTP connection failed, please check the code!')
    else:
        print(ftp.getwelcome()) # 打印登陆成功后的欢迎信息
        print('+------- ftp connection successful!!! --------+')
        return ftp

# 下载单个文件
def ftpDownloadFile(ftp, ftpfile, localfile):
    # fid = open(localfile, 'wb') # 以写模式打开本地文件
    bufsize =  1024
    with open(localfile, 'wb') as fid:
        ftp.retrbinary('RETR {0}'.format(ftpfile), fid.write, bufsize) # 接收服务器文件并写入本地文件
    return True

# 下载整个目录下的文件
def ftpDownload(ftp, ftpath, localpath):
	print('Remote Path: {0}'.format(ftpath))
	if not os.path.exists(localpath):
		os.makedirs(localpath)
	ftp.cwd(ftpath)
	print('+---------- downloading ----------+')
	#print(ftp.nlst())
	for file in ftp.nlst():
		print(file)
		if 'BRDC00IGS_R' in file:
			local = os.path.join(localpath, file)
			if os.path.isdir(file):           # 判断是否为子目录
				if not os.path.exists(local):
					os.makedirs(local)
				ftpDownload(ftp, file, local) # 递归调用
			else:
				ftpDownloadFile(ftp, file, local)
				un_gz(file)
		else:
			continue
	ftp.cwd('..')
	ftp.quit()
	return True

# 退出ftp连接
def ftpDisConnect(ftp):
	try:
		ftp.quit()
	except:
		print("close error")
             
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
	#print(str(utc_st))
	utc_year_str = (str(utc_st))[0:4]
	utc_day_int = int(utc_str.split( )[0])
	utc_day_str = str(utc_day_int + 1)

	return utc_day_str,utc_year_str

# 程序入口
if __name__ == '__main__':
	# 输入参数
	ftpserver = 'cddis.gsfc.nasa.gov'
	port = 21
	usrname = ''
	pwd = ''
	localpath = './data/'
	dir,files = file_search('./',1)
	print(dir)
	print(files)
	for file in files:
		if ('novatel' in file) and ('.bin' in file):
			print("select file is: %s" % file)
			file_time = file[-23:-4]
			time_list = file_time.split('_')
			print(time_list)
	utc_day,utc_year = get_utc_day(time_list)
	print("utc_day = %s,utc_year = %s" % (utc_day,utc_year))
	#ftpath = os.path.join('gnss','data','daily' + utc_year,utc_day,'20p')
	ftpath = '/gnss/data/daily/' + utc_year + '/' + utc_day + '/' + '20p/'
	print(ftpath)
	ftp = ftpConnect(ftpserver, 21, usrname, pwd)
	flag = ftpDownload(ftp, ftpath, localpath)
	print(flag)
	ftpDisConnect(ftp)
	print("+-------- OK!!! --------+\n")

