#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import time

ld_file_path = "ldscripts/stm32f469.ld"
map_file_path = "imu.map"
startup_file_path = "./.pio/libdeps/OpenRTK/STM32F469/CMSIS/startup_stm32f469xx.s"

fs_ld = open(ld_file_path)
fs_map = open(map_file_path)
fs_s = open(startup_file_path)

line = fs_ld.readline()
line_count = 0
while line:
	str = line.split( )
	if len(str) > 0:
		if str[0] == "FLASH":
			print str[1]
			break
	line = fs_ld.readline()  
fs_ld.close()