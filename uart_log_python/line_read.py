#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import time


key_world = 'txt'
file_list = []

def foreach_txt(rootDir,file):
    print "start..."
    start_time = time.time()
    list1=[]
    for root,dirs,files in os.walk(rootDir):
		files = sorted(files,key=lambda x: os.path.getmtime(os.path.join(rootDir, x)))
		for filename in files:
			result = key_world in filename		
			if result != True:
				continue
			filepath = os.path.join(root, filename)
			file_list.append(filepath)
    end_time = time.time()
    #print "end,%.2fs" % (end_time - start_time)
	
	
foreach_txt('./',".txt")
for i in range(len(file_list)):
	print "%d  - %s\r\n" % (i, file_list[i])
print "select txt"
txt_file = raw_input()
fh = open(file_list[int(txt_file)],"r")
line = fh.readline()
line_count = 0
while line:
	if len(line) > 37:
		print line
	line = fh.readline()  
	line_count = line_count + 1
fh.close
print("total line ",line_count)