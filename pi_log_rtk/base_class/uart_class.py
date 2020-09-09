import serial
import binascii
import time
from time import sleep
import datetime
import json
import os
import serial.tools.list_ports
#import thread
import threading
import platform

def os_detelt():
	print(platform.system())
	if(platform.system()=='Windows'):
		print('Windows')
		return 'win'
	elif(platform.system()=='Linux'):
		print('Linux')
		return 'linux'
	else:
		print('other')
		return 'other'



def print_serial(port):
	print("---------------[ %s ]---------------" % (port.name))
	print("Path: %s" % (port.device))
	print("Descript: %s" % (port.description))
	print("HWID: %s" % (port.hwid))
	if not None == port.manufacturer:
		print("Manufacture: %s" % (port.manufacturer))
	if not None == port.product:
		print("Product: %s" % (port.product))
	if not None == port.interface:
		print("Interface: %s" % (port.interface))
	print()

def detect_serials():
	#print ("start search serials")
	ports = serial.tools.list_ports.comports()
	port_cnt = 0
	port_list = []
	port_num = []
	os = os_detelt()
	for port in ports:
		if (os == 'linux'):
			if (('USB' in str(port)) == False):
				continue
		#print_serial(port)
		port_str = str(port.device)
		#print (port_str)
		if (os == 'linux'):
			port_num.append(int(port_str[11:]))	#linux
		elif (os == 'win'):
			port_num.append(int(port_str[3:]))		#windows
		port_list.append(port.device)
		port_num.sort()
		port_cnt += 1
		#print (port)
	print ('ports[0] = %s' % ports[0])
	return (port_cnt, port_list,port_num)

class uart_communicate():
	def __init__(self,com,baud,timeout,is_log,file_name):
		self.port = com
		self.baud = baud
		self.timeout =timeout
		self.is_log = is_log
		self.file_name = file_name
		print("self.file_name = %s" % self.file_name)
		self.file_init_flag = False
		self.is_connect = False
		global ret
		try:
			self.serial_handle= serial.Serial(self.port,self.baud,timeout=self.timeout)
			if (self.serial_handle.is_open):
				ret = True
				self.is_connect = True
		except Exception as e:
			print(" error ",e)

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
	def print_time(self):
		while True:
			print (self.file_name)
			time.sleep(0.6)
	def recive_data(self,receive_type):
		#threading.start_new_thread(self.print_time, ("Thread-1", 2, ) )
		#t = threading.Thread(target=self.print_time())
		#t.start() 
		'''
		while True:
			print (self.file_name)
			time.sleep(0.6)
		'''
		
		print("start receive data")
		while True:
			try:
				if self.serial_handle.in_waiting:
					if(receive_type == 0):
						for i in range(self.serial_handle.in_waiting):
							data1 = self.serial_handle.read_size(1).hex()
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
