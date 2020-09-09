from socket import *
import time
import socket


def encode(src):    
	src = src.ljust(15,"\x20")
	src = src.ljust(16,"\x00")
	print(src)
	print(len(src))
	names = []
	for c in src:
		char_ord = ord(c)
		high_4_bits = char_ord >> 4
		low_4_bits = char_ord & 0x0f
		names.append(high_4_bits)
		names.append(low_4_bits)
		res = ""    
		#print(names)
	for name in names:
		res += chr(0x41+name)
	return res

host_name = (encode('OPENRTK'))
# -*- coding: utf-8 -*-
print(host_name)



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
PORT = 137
network = '<broadcast>'
# 发送数据:
#s.sendto(u"test123456789".encode("utf-8"), (network, PORT))
buf_size = 1024
while True:
	data = host_name
	print(data)
	s.sendto(data.encode("utf-8"), ('192.168.137.255', PORT))
	s.sendto(data.encode("utf-8"), ('192.168.137.255', PORT))
	#s.sendto((data).encode('utf-8'), ('192.168.137.255', PORT))
	data_rev, ADDR = s.recvfrom(buf_size)
	if not data:
		break
	print("get：", data_rev)
s.close()
