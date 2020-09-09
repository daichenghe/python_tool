#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import time
import binascii  

ld_file_path = "ldscripts/stm32f469.ld"
map_file_path = "./imu.map"
startup_file_path = "./.pio/libdeps/OpenRTK/STM32F469/CMSIS/startup_stm32f469xx.s"

fs_ld = open(ld_file_path,'r')
fs_map = open(map_file_path,'r')
fs_s = open(startup_file_path,'r')


line_count = 0
text_read_flag = 0
rodata_read_flag = 0
#map_dict = { 'BASE_MEMORY':{'FLASH_ORIGIN':'', 'FLASH_LENGTH':'', 'RAM_ORIGIN':'', 'RAM_LENGTH':'','CCMRAM_ORIGIN':'',"CCMRAM_LENGTH":''},\
map_dict = { 'BASE_MEMORY':{'FLASH_ORIGIN':'', 'FLASH_LENGTH':'', 'RAM_ORIGIN':'','RAM_LENGTH':'','CCMRAM_ORIGIN':'',"CCMRAM_LENGTH":''},\
'FLASH':{'isr_vector_start':'', 'isr_vector_end':'', '.text_start':'', '.text_end':'','.rodata_start':'',".rodata_end":'',\
'.extab_start':'','.extab_end':'','_sidata_start':'','_sidata_end':'','_siccmram_start':'','_siccmram_end':''},\
'RAM':{'.data_start':'', '.data_end':'', '.bss_start':'', '.bss_end':'','.heap_start':'',".heap_end":'','.stack_start':'',".stack_end":''},\
'ccmram':{'.ccmram_start':'', '.ccmram_end':''},\
'freertos':{'.ucHeap_start':'', '.ucHeap_end':''}}

line = fs_ld.readline()
while line:
	str = line.split( )
	if len(str) > 0:
		#if str[0] == "FLASH":
		if ("_estack" in line):
			map_dict['RAM']['.heap_end'] = str[2]
			map_dict['RAM']['.stack_start'] = str[2]
		if ("FLASH (rx)" in line):
			map_dict['BASE_MEMORY']['FLASH_ORIGIN'] = str[5][:-1]
			map_dict['BASE_MEMORY']['FLASH_LENGTH'] = str[8]
			#print map_dict
		elif ("RAM (xrw)" in line):
			map_dict['BASE_MEMORY']['RAM_ORIGIN'] = str[5][:-1]
			map_dict['BASE_MEMORY']['RAM_LENGTH'] = str[8]
		elif ("CCMRAM (rw)" in line):
			map_dict['BASE_MEMORY']['CCMRAM_ORIGIN'] = str[5][:-1]
			map_dict['BASE_MEMORY']['CCMRAM_LENGTH'] = str[8]
			break
	line = fs_ld.readline()  
fs_ld.close()
	
line = fs_map.readline()
line_num = 1
while line:
	str = line.split( )
	if line:
		if (".isr_vector" in line):
			if len(str) > 3:
				map_dict['FLASH']['isr_vector_start'] = str[1]
				map_dict['FLASH']['isr_vector_end'] = str[2]
		elif (".text" in line):
			if text_read_flag == 0:
				map_dict['FLASH']['.text_start'] = str[1]
				map_dict['FLASH']['.text_end'] = str[2]
				text_read_flag = 1
		elif ("*(.rodata)" in line):
			print "--------------------------------------------------------------------"
			if rodata_read_flag == 0:
				'''
				file_num = fs_map.tell()
				print "file_num: %d" % file_num
				fs_map.seek(file_num - len(line))
				'''
				file_num = fs_map.tell()
				fs_map.seek(0)
				all_line = fs_map.readlines()
				
				#print all_line[line_num - 3]
				str = all_line[line_num - 3].split( )
				map_dict['FLASH']['.rodata_start'] = str[1]
				#map_dict['FLASH']['.rodata_end'] = str[2]
				print str[1]
				print str[2]
				fs_map.seek(file_num)
				rodata_read_flag = 1
		elif (".ARM.exidx" in line):
			if len(str) > 2:
				map_dict['FLASH']['.rodata_end'] = str[1]
				map_dict['FLASH']['.extab_start'] = str[1]
		elif("__exidx_end" in line):
				map_dict['FLASH']['.extab_end'] = str[0]				
		elif ("_sidata" in line):
			map_dict['FLASH']['_sidata_start'] = str[0]
		elif ("_siccmram" in line):
			map_dict['FLASH']['_siccmram_start'] = str[0]
		elif ("_sdata" in line):
			map_dict['RAM']['.data_start'] = str[0]
		elif ("_edata" in line):
				map_dict['RAM']['.data_end'] = str[0]
				sidata_s = int(map_dict['FLASH']['_sidata_start'], 16)
				sidata_len = int(map_dict['RAM']['.data_end'], 16) - int(map_dict['RAM']['.data_start'], 16)
				sidata_e = sidata_s + sidata_len
				
				print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
				sidata_end_hex = hex(sidata_e)
				print sidata_end_hex
				map_dict['FLASH']['_sidata_end'] = sidata_end_hex
		elif ("_sbss" in line):
				map_dict['RAM']['.bss_start'] = str[0]
		elif ("_ebss" in line):
				map_dict['RAM']['.bss_end'] = str[0]
		elif ("_user_heap_stack" in line):
			line = fs_map.readline() 
			str = line.split( )
			map_dict['RAM']['heap_start'] = str[0]
			map_dict['RAM']['stack_end'] = str[0]
			print map_dict
		elif ("_sccmram" in line):
			map_dict['ccmram']['.ccmram_start'] = str[0]
		elif ("_eccmram" in line):
			map_dict['ccmram']['.ccmram_end'] = str[0]	
			ccm_s = int(map_dict['FLASH']['_siccmram_start'], 16)
			ccm_len = int(map_dict['ccmram']['.ccmram_end'], 16) - int(map_dict['ccmram']['.ccmram_start'], 16)
			ccm_e = ccm_s + ccm_len
			print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
			ccm_e_hex = hex(ccm_e)
			print sidata_end_hex
			map_dict['ccmram']['.ccmram_end'] = ccm_e_hex
		elif (".bss.ucHeap" in line):
			map_dict['freertos']['.ucHeap_start'] = str[1]	
			start = int(str[1], 16)
			len = int(str[2], 16)
			end = start + len
			end_hex = hex(end)
			print end_hex
			print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
			map_dict['freertos']['.ucHeap_end'] = end_hex
		#elif 
	line = fs_map.readline()  
	line_num += 1
fs_map.close()