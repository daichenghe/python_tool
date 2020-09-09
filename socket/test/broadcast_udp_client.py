# -*- coding: utf-8 -*-

import socket

'''
客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据：
D0 16 01 10 00 01 00 00 00 00         Ð.........
2001f9b0: 00 00 20 45 50 46 41 45 46 45 4F 46 43 46 45 45   ...EPFAEFEOFCFEE
2001f9c0: 4C 43 41 43 41 43 41 43 41 43 41 43 41 43 41 43   LCACACACACACACAC
2001f9d0: 41 41 41 00 00 20 00 01 8C A4 D2 03 9F BF 48 31   AAA......¤Ò..¿H1
2001f9e0: 9C F3 34 E6
'''

default_bios = [0xD0,0x16,0x01,0x10,0x00,0x01,0x00,0x00,0x00,0x00,\
0x00,0x00,0x20,0x45,0x50,0x46,0x41,0x45,0x46,0x45,0x4F,0x46,0x43,0x46,0x45,0x45,\
0x4C,0x43,0x41,0x43,0x41,0x43,0x41,0x43,0x41,0x43,0x41,0x43,0x41,0x43,0x41,0x43,\
0x41,0x41,0x41,0x00,0x00,0x20,0x00,0x01,0x8C,0xA4,0xD2,0x03,0x9F,0xBF,0x48,0x31,\
0x9C,0xF3,0x34,0xE6]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
PORT = 137
network = '<broadcast>'
# 发送数据:
#s.sendto(u"test123456789".encode("utf-8"), (network, PORT))
buf_size = 1024
while True:
	data = input('>')
	#s.sendto("udp_test111\r\n".encode("utf-8"), ('192.168.137.255', PORT))
	s.sendto(bytes(default_bios), ('192.168.137.255', PORT))
	data_rev, ADDR = s.recvfrom(buf_size)
	print(len(data_rev))
	print(int(data_rev[len(data_rev) - 1]))
	if not data:
		break
	print("get：", data_rev)
s.close()