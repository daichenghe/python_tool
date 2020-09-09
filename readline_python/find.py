# -*- coding:utf-8 -*-

import os
import time

fh = open("text.txt", "r")
line = fh.readline()
line_count = 0
while line:
	if len(line) > 85 or len(line) < 80:
		print line
	dir = line.find("-")
	if dir > 0:
		print dir
	line = fh.readline()  
	line_count = line_count + 1
fh.close()
print("total line ",line_count)
