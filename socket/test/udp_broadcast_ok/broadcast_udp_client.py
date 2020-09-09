# -*- coding: utf-8 -*-

import socket

'''
客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据：
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
PORT = 137
network = '<broadcast>'
# 发送数据:
#s.sendto(u"test123456789".encode("utf-8"), (network, PORT))
buf_size = 1024
while True:
	data = input('>')
	s.sendto("udp_test\r\n".encode("utf-8"), ('192.168.137.255', PORT))
	#s.sendto((data).encode('utf-8'), ('192.168.137.255', PORT))
	data_rev, ADDR = s.recvfrom(buf_size)
	if not data:
		break
	print("get：", data_rev)
s.close()