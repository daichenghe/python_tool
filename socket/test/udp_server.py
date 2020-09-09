# -*- coding: utf-8 -*-
import ctypes
import socket

# ipv4        SOCK_DGRAM指定了这个Socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# 绑定 客户端口和地址:
s.bind(('', 9999))
print ('Bind UDP on 9999...')
while True:
    # 接收数据 自动阻塞 等待客户端请求:
    data, addr = s.recvfrom(1024)
    message = 'Received from %s:%s.' % (addr, data)
    print (message)
    ctypes.windll.user32.MessageBoxA(0, data.decode("utf-8").encode('gb2312'), u' 信息'.encode('gb2312'), 0)