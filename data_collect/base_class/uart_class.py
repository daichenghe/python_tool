import serial
import binascii
import time
from time import sleep
import datetime
import json
import os
import serial.tools.list_ports

class uart_communicate():
	def __init__(self,com,baud,timeout,is_log,file_name):
		self.port = com
		self.baud = baud
		self.timeout =timeout
		self.is_log = is_log
		self.file_name = file_name
		self.file_init_flag = False
		self.is_connect = False
		global ret
		try:
			self.serial_handle= serial.Serial(self.port,self.baud,timeout=self.timeout)
			if (self.serial_handle.is_open):
				ret = True
				self.is_connect = True
		except Exception as e:
			print("---error---：", e)

	# message
	def print_name(self):
		print(self.serial_handle.name) 
		print(self.serial_handle.port)
		print(self.serial_handle.baudrate)
		print(self.serial_handle.bytesize)
		print(self.serial_handle.parity)
		print(self.serial_handle.stopbits)
		print(self.serial_handle.timeout)
		print(self.serial_handle.writeTimeout)
		print(self.serial_handle.xonxoff)
		print(self.serial_handle.rtscts)
		print(self.serial_handle.dsrdtr)
		print(self.serial_handle.interCharTimeout)

	#open
	def open_serial(self):
		self.serial_handle.open()

	#close
	def close_serial(self):
		self.serial_handle.close()
		print(self.serial_handle.is_open)  

	# print port
	@staticmethod
	def print_used_com():
		port_list = list(serial.tools.list_ports.comports())
		print(port_list)

	#read
	def read_size(self,size):
		return self.serial_handle.read(size=size)
	def read_all(self,size):
		return self.serial_handle.read_all()
	#read line
	def read_line(self):
		return self.serial_handle.readline()

	#send
	def send_data(self,data):
		self.serial_handle.write(data)

	# self.serial_handle.write(chr(0x06).encode("utf-8"))  
	# print(self.serial_handle.read().hex()) 
	# print(self.serial_handle.read())
	# print(self.serial_handle.read(10).decode("gbk"))
	# print(self.serial_handle.readline().decode("gbk"))
	# print(self.serial_handle.readlines())
	# print(self.serial_handle.in_waiting)
	# print(self.serial_handle.out_waiting)
	# print(self.serial_handle.readall())

	#read while
	def log_file_close(self):
		self.fh.close()
		print('close')
	def recive_data(self,receive_type):
		print("start receive data")
		while True:
			try:
				if self.serial_handle.in_waiting:
					if(receive_type == 0):
						for i in range(self.serial_handle.in_waiting):
							data1 = self.read_size(1).hex()
							data2 = int(data1,16)
							if (data2 == "exit"): 
								break
							else:
								 pass
					if(receive_type == 1):
						data = self.serial_handle.read_all()
						if (data == "exit"):
							break
						else:
							if data != '' and self.file_init_flag == False:
								self.fh = open(self.file_name,"wb")
								self.file_init_flag = True
							if self.file_init_flag == True:
								self.fh.write(data)
							 #print("data:", data)
			except Exception as e:
				print("error",e)

'''
uart_communicate.print_used_com()
ret = False 

serial = uart_communicate("com15",460800,0.5,True,'123.txt')
if (serial.is_connect):
    serial.recive_data(1)
'''