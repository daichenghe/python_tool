#!/usr/bin/python
#-*- coding: utf-8 -*-

import os
import time
import binascii 
import csv


map_dict = { 'BASE_MEMORY':{'FLASH_ORIGIN':'', 'FLASH_LENGTH':'', 'RAM_ORIGIN':'','RAM_LENGTH':'','CCMRAM_ORIGIN':'',"CCMRAM_LENGTH":''},\
'FLASH':{'isr_vector_start':'', 'isr_vector_end':'', '.text_start':'', '.text_end':'','.rodata_start':'',".rodata_end":'',\
'.extab_start':'','.extab_end':'','_sidata_start':'','_sidata_end':'','_siccmram_start':'','_siccmram_end':''},\
'RAM':{'.data_start':'', '.data_end':'', '.bss_start':'', '.bss_end':'','.heap_start':'',".heap_end":'','.stack_start':'',".stack_end":''},\
'ccmram':{'.ccmram_start':'', '.ccmram_end':''},\
'freertos':{'.ucHeap_start':'', '.ucHeap_end':''}}

def get_str(main_key,sub_key1,sub_key2):
	return ',' + map_dict[main_key][sub_key1] + ',' + map_dict[main_key][sub_key2] + ',' #+ '\r\n'


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
				isr_vec_len = int(str[2],16)
				isr_vec_s = int(str[1],16)
				isr_vec_end = isr_vec_s + isr_vec_len
				isr_vec_end_hex = hex(isr_vec_end)
				map_dict['FLASH']['isr_vector_end'] = isr_vec_end_hex
		elif ("*(.text)" in line):									#TODO:
			line = fs_map.readline()
			str = line.split( )
			if text_read_flag == 0:
				map_dict['FLASH']['.text_start'] = str[1]
				#map_dict['FLASH']['.text_end'] = str[2]
				text_read_flag = 1
		elif ('_etext' in line):
			map_dict['FLASH']['.text_end'] = str[0]
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
				print all_line[line_num - 2]
				str = all_line[line_num - 2].split( )
				map_dict['FLASH']['.rodata_start'] = str[1]
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
			print str[0]
			map_dict['RAM']['.heap_start'] = str[0]
			map_dict['RAM']['.stack_end'] = str[0]
		elif ("_sccmram" in line):
			map_dict['ccmram']['.ccmram_start'] = str[0]
		elif ("_eccmram" in line):				#TODO:
			map_dict['ccmram']['.ccmram_end'] = str[0]	
			ccm_s = int(map_dict['FLASH']['_siccmram_start'], 16)
			
			ccm_len = int(map_dict['ccmram']['.ccmram_end'], 16) - int(map_dict['ccmram']['.ccmram_start'], 16)
			ccm_e = ccm_s + ccm_len
			print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
			ccm_e_hex = hex(ccm_e)

			#siccmram_end_hex = map_dict['FLASH']['_siccmram_start'] + hex(ccm_len)
			#print siccmram_end_hex
			map_dict['FLASH']['_siccmram_end'] = ccm_e_hex
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
print map_dict['BASE_MEMORY']
print map_dict['FLASH']
print map_dict['RAM']
print map_dict['ccmram']
print map_dict['freertos']




fs_save = open("map.csv","w")
fs_save.write("MEMORY,ORIGIN,LENGTH\r\n")


#str_to_write = 'FLASH,' + map_dict['BASE_MEMORY']['FLASH_ORIGIN'] +',' + map_dict['BASE_MEMORY']['FLASH_ORIGIN'] + '\r\n'
memory_to_write = 'FLASH' + get_str('BASE_MEMORY','FLASH_ORIGIN','FLASH_LENGTH') + '\r\n'
memory_to_write += 'RAM' + get_str('BASE_MEMORY','RAM_ORIGIN','RAM_LENGTH') + '\r\n'
memory_to_write += 'CCMRAM' + get_str('BASE_MEMORY','CCMRAM_ORIGIN','CCMRAM_LENGTH') + '\r\n\r\n'
fs_save.write(memory_to_write)


fs_save.write("FLASH,START,END,SIZE\r\n")
isr_note = '中断向量表\r\n'
text_note = '代码段\r\n'
rodata_note = '常量\r\n'
extab_note = '堆栈回溯，未使用\r\n'
sidata_note = '存放ram中初始化为非0的全局变量和静态变量的初始化值(启动文件中通过CopyDataInit函数复制到RAM的.data段)\r\n'
siccmram_note = '存放ccmram中初始化为非0的全局变量和静态变量的初始化值，目前启动文件中未将此部分数据搬运到ccmram，谨慎使用\r\n'


flash_to_write = 'isr_vector' + get_str('FLASH','isr_vector_start','isr_vector_end') + isr_note
flash_to_write += 'text' + get_str('FLASH','.text_start','.text_end') + text_note
flash_to_write += 'rodata' + get_str('FLASH','.rodata_start','.rodata_end') + rodata_note
flash_to_write += 'extab' + get_str('FLASH','.extab_start','.extab_end') + extab_note
flash_to_write += 'sidata' + get_str('FLASH','_sidata_start','_sidata_end') + sidata_note
flash_to_write += '_siccmram' + get_str('FLASH','_siccmram_start','_siccmram_end') + siccmram_note + '\r\n\r\n'
fs_save.write(flash_to_write)


fs_save.write("RAM,START,END,SIZE\r\n")
data_note = 'RAM data段\r\n'
bss_note = 'RAM bss段,启动文件中调用FillZerobss使之全部初始化为0\r\n'
heap_note = 'heap\r\n'
stack_note = 'stack段\r\n'


ram_to_write = 'data' + get_str('RAM','.data_start','.data_end') + data_note
ram_to_write += 'bss' + get_str('RAM','.bss_start','.bss_end') + bss_note
ram_to_write += 'heap' + get_str('RAM','.heap_start','.heap_end') + bss_note
ram_to_write += 'stack' + get_str('RAM','.stack_start','.stack_end') + stack_note + '\r\n\r\n'
fs_save.write(ram_to_write)


fs_save.write("CCMRAM,START,END,SIZE\r\n")
ccmram_note = 'ccmram 变量初始化值未搬运，谨慎使用\r\n'
ccmram_ro_write = 'ccmram' + get_str('ccmram','.ccmram_start','.ccmram_end') + ccmram_note + '\r\n\r\n'
fs_save.write(ccmram_ro_write)


fs_save.write("FREERTOS,START,END,SIZE\r\n")
rtos_note = 'freertos各任务的堆栈从此分配\r\n'
rtos_to_write = 'ccmram' + get_str('freertos','.ucHeap_start','.ucHeap_end') + rtos_note
fs_save.write(rtos_to_write)


fs_ld.close()
fs_map.close()
fs_s.close()
fs_save.close()