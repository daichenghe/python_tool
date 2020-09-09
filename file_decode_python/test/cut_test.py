# -*- coding:utf-8 -*-
#将所有TXT连接成一个，并删除掉重复记录
import os
import time
def BianLi(rootDir):
    print "start..."
    start_time = time.time()
    fh = open("all.txt", "w")
    list1=[]
    for root,dirs,files in os.walk(rootDir):
#	for files in os.walk(rootDir):
		for filename in files:
			print filename
			result = "test" in filename
			if result != True:
				continue
			filepath = rootDir + filename
			file = open(filepath, 'r')
			str = file.read()
			print str
			str_to_write = str.split('aaaaaaaaaaa',1);
			print "split:",str_to_write[0]
#			list1.append(line)
			fh.write(str_to_write[1])
    fh.close()
    end_time = time.time()
    print "end,%.2fs" % (end_time - start_time)
rootDir = '../'
BianLi(rootDir)