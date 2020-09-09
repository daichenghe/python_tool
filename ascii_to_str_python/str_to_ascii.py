# -*- coding:utf-8 -*-
import os
import time

import numpy as np
print("put your str")
str = raw_input()
test = ''
for c in str:
	test = test + hex(ord(c))#.replace('0x', '')
	test = test + ','
print test	
ascii = np.fromstring(str, dtype=np.uint8)
print(ascii)