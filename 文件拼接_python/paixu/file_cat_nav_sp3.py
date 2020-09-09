# -*- coding:utf-8 -*-
#将所有TXT连接成一个，并删除掉重复记录
import os
import time
import os, glob, time

def search_all_files_return_by_time_reversed(path, reverse=True):
	for root,dirs,files in os.walk(path):
	
    return sorted(files, key=lambda x: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(x))), reverse=False)

def foreach(rootDir,file,for_file):
	print "start..."
	start_time = time.time()
	fh = open("file_cat.txt", "w")
	for filename in for_file:
		print filename
	
		result = key_world in filename
		if result != True:
			continue
		print "for each file!!!!",filename	
		filepath = os.path.join(root, filename)
		print filepath
		file = open(filepath, 'r')
		str_ori = file.read()
		str = str_ori.replace("EOF", " ")
		str_to_write = str.split('''/* CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
/* CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
/* CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC''',1);
		if file_start == 0:
			global file_start
			fh.write(str)
			file_start+= 1
		else:
			fh.write(str_to_write[1])
	fh.close()
	end_time = time.time()
	print "end,%.2fs" % (end_time - start_time)

rootDir = '../'
file_start = 0
key_world = raw_input("please enter:")
txt_file = key_world + ".txt"
all_file = search_all_files_return_by_time_reversed("../")
print all_file
foreach(rootDir,txt_file,all_file)