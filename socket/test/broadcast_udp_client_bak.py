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
s.sendto(u"my_test".encode("utf-8"), ('192.168.137.255', PORT))

s.close()