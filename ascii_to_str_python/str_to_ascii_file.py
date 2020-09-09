# -*- coding:utf-8 -*-
import os
import time

import numpy as np
print("put your str")
fh = open("config_html.txt", "r")
str = fh.read()
fs = open("config_ascii","w")
test = ''
i = 0
for c in str:
	hex_str = hex(ord(c))
	if len(hex_str) < 4:
		list_str = list(hex_str)
		list_str.insert(2, '0')
		str_in = ''.join(list_str)
	else:
		str_in = hex_str
	test = test + str_in #hex(ord(c))#.replace('0x', '')
	test = test + ','
	i = i+1
	if i==16:
		test = test + "\n"
		i=0
print test	
fs.write(test)
fs.close()
fh.close()
ascii = np.fromstring(str, dtype=np.uint8)
print(ascii)