#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 17:28
# @Author  : zengsk in HoHai

import os
import sys
from ftplib import FTP
import gzip


def un_gz(file_name):
	print("un_gz)
	f_name = file_name.replace(".gz", "")
	g_file = gzip.GzipFile(file_name)
	open(f_name, "wb+").write(g_file.read())
	g_file.close()


# 连接ftp服务器
def ftpConnect(ftpserver, port, usrname, password):
    ftp = FTP()
    try:
        ftp.connect(ftpserver, port)
        ftp.login(usrname, password)
    except:
        raise IOError('\n FTP connection failed, please check the code!')
    else:
        print(ftp.getwelcome()) # 打印登陆成功后的欢迎信息
        print('\n+------- ftp connection successful!!! --------+')
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
	for file in ftp.nlst():
		print(file)
		local = os.path.join(localpath, file)
		if os.path.isdir(file):           # 判断是否为子目录
			if not os.path.exists(local):
				os.makedirs(local)
			ftpDownload(ftp, file, local) # 递归调用
		else:
			ftpDownloadFile(ftp, file, local)
			un_gz(file)
	ftp.cwd('..')
	ftp.quit()
	return True

# 退出ftp连接
def ftpDisConnect(ftp):
    ftp.quit()
             
# 程序入口
if __name__ == '__main__':
    # 输入参数
    ftpserver = 'jsimpson.pps.eosdis.nasa.gov'
    port = 21
    usrname = 'xxxxxx@gmail.com'
    pwd = 'xxxxxxxxxxxxxx'
    ftpath = '/NRTPUB/imerg/late/201403/'
    localpath = 'D:/data/'
  
    ftp = ftpConnect(ftpserver, 21, usrname, pwd)
    flag = ftpDownload(ftp, ftpath, localpath)
    print(flag)
    ftpDisConnect(ftp)
    print("\n+-------- OK!!! --------+\n")

