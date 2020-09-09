# -*- coding:utf-8 -*-

import os
import time
import binascii   

import math
import serial
import serial.tools.list_ports
import struct


fh = open("sensor", "rb")
bin = fh.read()
count_old = 0
count = 0
count_gps = 0
fmt = ''
fmt += 'BBBB'     
fmt += 'H'        # header_length
fmt += 'B'        #	message type
fmt += 'B'        # port_address
fmt += 'H'        # message_length
fmt += 'H'        # sequence
fmt += 'B'        # idle
fmt += 'B'        # time_status
fmt += 'H'        # gps_week
fmt += 'I'        # gps_millisecs
time_old = 0
first_run = 0
start_week = 0
start_ms = 0
end_week = 0
end_ms = 0
count_error = 0
count_9 = 0
count_11 = 0
for i in range(len(bin) - 3):
	#print(ord(bin[i]))

	hex1 = binascii.b2a_hex(bin[i])
	hex2 = binascii.b2a_hex(bin[i+1])
	hex3 = binascii.b2a_hex(bin[i+2])

	#print hex and (hex4 == '')
	if (hex1 == 'aa') and (hex2 == '44') and (hex3 == '12') :

		data = struct.unpack(fmt, bin[i:i+20])

		#print "type"

		if data[4] == 268:
			count = count+1
			#print data[11]
			#print data[12]
			if (data[12] - time_old) == 9:
				print "min 9 \r\n"
				for j in range(13):
					print data[j]
				count_9 += 1
			if (data[12] - time_old) == 11:
				print "max 11 \r\n"
				for j in range(13):
					print data[j]
				count_11 += 1
			if ((data[12] - time_old) < 9) or ((data[12] - time_old) > 11) :
				#print "test"
				print data[12] - time_old
				count_error += 1
			time_old = data[12]
			#print data[13]
			#print count_old
			sub = i-count_old
			if first_run == 0:
				start_ms = data[12]
				first_run = 1
			end_ms = data[12]
		if data[4] == 42:
			count_gps = count_gps + 1
		#print sub
		'''
		if ((sub) > 72) :
			print sub
			print i
		count_old = i
		'''
fh.close()
print "total sensor %d" % count
print  "total gps %d" % count_gps
#print start_ms
#print end_ms
print "total time %d" % (end_ms - start_ms)
print "total error 9 %d" % count_9
print "total error 11 %d" % count_11
print "total error %d" % count_error


