# -*- coding: utf-8 -*-
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
*
* Copyright (c) 2020-2020  ACEINNA 
* Wuxi ACEINNA Sensing Technology.版权所有 2020-2020
*
* PROPRIETARY RIGHTS of ACEINNA Company are involved in the  　　　　　　
* subject matter of this material.  All manufacturing, reproduction, use,
* and sales rights pertaining to this subject matter are governed by the
* license agreement.  The recipient of this software implicitly accepts
* the terms of the license.
* 本软件文档资料是新纳公司的资产,任何人士阅读和使用本资料必须获得
* 相应的书面授权,承担保密责任和接受相应的法律约束.
*
********************************************************************************
* File Name          : rtk_upload.py
* Author             : dch
* Revision           : 1.0 
* Date               : 09/05/2015
* Description        : rtk upgrade thread
*
* HISTORY***********************************************************************
* 09/05/2020  | created                                | dch
*
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import serial
import binascii
from time import sleep
import os 
import sys
import time

def calc_crc(payload):
	'''Calculates CRC per 380 manual
	'''
	crc = 0x1D0F
	for bytedata in payload:
		crc = crc^(bytedata << 8) 
		for i in range(0,8):
			if crc&0x8000:
				crc = (crc << 1)^0x1021
			else:
				crc = crc << 1
	crc = crc & 0xffff
	return crc

def start_bootloader(serial):
    '''Starts bootloader
        :returns:
            True if bootloader mode entered, False if failed
    '''
    C = [0x55, 0x55, ord('J'), ord('I'), 0x00 ]
    crc = calc_crc(C[2:4] + [0x00])    # for some reason must add a payload byte to get correct CRC
    crc_msb = (crc & 0xFF00) >> 8
    crc_lsb = (crc & 0x00FF)
    C.insert(len(C), crc_msb)
    C.insert(len(C), crc_lsb)
    serial.write(C)
    #print (C)
    sleep(2)   # must wait for boot loader to be ready
    #R = serial.read(5)
    R = serial.read_all()   #7
    #print(R)
    try:
        if R[0] == 85 and R[1] == 85:

            packet_rev = chr(R[0]) + chr(R[1])
            packet_type = R[2] + R[3]
            #print(packet_rev)
            if (packet_type == 'JI') or (packet_rev == 'UU'):
                serial.read(R[4]+2)
                #print('bootloader ready')
                sleep(2)
                return True
            else: 
                return False
        else:
            return False
    except:
        return False



def start_app(serial):
	'''Starts app
	'''
	C = [0x55, 0x55, ord('J'), ord('A'), 0x00 ]
	crc = calc_crc(C[2:4] + [0x00])    # for some reason must add a payload byte to get correct CRC
	crc_msb = (crc & 0xFF00) >> 8
	crc_lsb = (crc & 0x00FF)
	C.insert(len(C), crc_msb)
	C.insert(len(C), crc_lsb)
	serial.write(C)
	sleep(2)
	#print (C)
	R = serial.read_all()   #7
	'''
	if (R[0]) == 85 and (R[1]) == 85:
		packet_type =  R[2] + R[3]
		print(packet_type)
	'''
	if R[0] == 85 and R[1] == 85:
		packet_type = '{0:1c}'.format(R[2]) + '{0:1c}'.format(R[3])
		#print(packet_type)

def write_block(serial,buf, data_len, addr):
	'''Executed WA command to write a block of new app code into memory
	'''
	#print(data_len, addr)
	C = [0x55, 0x55, ord('W'), ord('A'), data_len+5]
	addr_3 = (addr & 0xFF000000) >> 24
	addr_2 = (addr & 0x00FF0000) >> 16
	addr_1 = (addr & 0x0000FF00) >> 8
	addr_0 = (addr & 0x000000FF)
	C.insert(len(C), addr_3)
	C.insert(len(C), addr_2)
	C.insert(len(C), addr_1)
	C.insert(len(C), addr_0)
	C.insert(len(C), data_len)
	for i in range(data_len):
		#C.insert(len(C), ord(buf[i]))
		C.insert(len(C), buf[i])
	crc = calc_crc(C[2:C[4]+5])  
	crc_msb = int((crc & 0xFF00) >> 8)
	crc_lsb = int((crc & 0x00FF))
	C.insert(len(C), crc_msb)
	C.insert(len(C), crc_lsb)
	status = 0
	while (status == 0):
		serial.write(C)
		test = []
		for ele in C:
			test.insert(len(test),hex(ele))
		#print test
		#print len(C)
		#print('percent: {:.2%}'.format(addr/fs_len))

		if addr == 0:
		   sleep(8)
		else:
		   #sleep(0.01)
		   sleep(0.05)
		#print('wait')
		#input()
		R = serial.read(12)  #longer response
		response=[]
		for ele in bytearray(R):
			response.append(ele)
		#print(response)
		#test = ord(R[0])
		status = 1
		if len(R) > 1 and (R[0]) == 85 and (R[1]) == 85:
			#packet_type =  '{0:1c}'.format(R[2]) + '{0:1c}'.format(R[3])
			#packet_type = R[2] + R[3]
			#print(packet_type)
			packet_type = '{0:1c}'.format(
				R[2]) + '{0:1c}'.format(R[3])
			if packet_type == 'WA':
				status = 1
			else:
				sys.exit()
				#print('retry 1')
				status = 0
		else:
			#self.reset_buffer()
			sleep(1)
			print('no packet')
			sys.exit()
		


def recv(serial):
	while True:
		if select == "2":
			data = binascii.b2a_hex(serial.read_all())
			file.write(data)
			#data = serial.read_all()
			#data = "test"
		else:
			#data = binascii.b2a_hex(serial.read_all())
			data = serial.read_all()
			file.write(data)
	return data

print('please set com')
com_set = input()
serial = serial.Serial(com_set, 115200, timeout=0.1)  #/dev/ttyUSB0
if __name__ == '__main__':

	if serial.isOpen() :
		print("open success")
		start_time = time.time()
	else :
		print("open failed")
	while True:
		sync = [0xfd,0xc6,0x49,0x28]
		#sync = [0x28,0x49,0xc6,0xfd]
		serial.write(sync)
		sleep(0.2)
		R = serial.read(4)
		print(len(R))
		if(R[0] == 0x3A) and (R[1] == 0x54) and (R[2] == 0x2c) and(R[3] == 0xA6):
			print('get sync')
			break
	while True:
		change_baud_cmd = [0x71]
		baud = [0x00,0x84,0x03,0x00]
		serial.write(change_baud_cmd)
		serial.write(baud)
		sleep(0.5)
		print("wait baud")
		R = serial.read(12)
		print(len(R))
		print(hex(R[0]))
		print(hex(R[1]))		
		if R[0] == 0xCC:
			print("change baud suc")
			serial.baudrate = 230400
			break
	while True:
		check_baud = 0x38
		print(serial.baudrate)
		while True:
			print("wait baud check")
			sleep(0.5)
			serial.write(check_baud)
			sleep(0.2)
			R = serial.read(1)
			print(len(R))
			if(len(R) > 0):
				print(hex(R[0]))
				if R[0] == 0xCC:
					print('check baud suc')
					break
		break
	while True:
		host_ready = 0x5a
		serial.write(host_ready)
		print('wait host ready')
		while True:
			sleep(0.5)
			R = serial.read(1)
			print(len(R))
			if(len(R) > 0):
				print(hex(R[0]))
				if R[0] == 0xCC:
					print('host ready')
					break
		break
		'''
		print(len(R))
		print(hex(R[0]))
		print(hex(R[1]))
		print(hex(R[2]))
		print(hex(R[3]))
		'''