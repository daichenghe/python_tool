# -*- coding:utf-8 -*-
import os
import time
import numpy as np
fh = open("image.txt","r")
fs = open("image_bin","wb")
str = fh.read()
str1 = str.replace(',','')
#fs.write(str)
print str1

ret = str.split(',')


for c in ret:
	#print c
	test = bin(int(c,16))
	fs.write(test)
	#print test