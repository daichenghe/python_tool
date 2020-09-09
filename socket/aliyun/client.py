#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket

s = socket.socket()
host = socket.gethostname()
port = 6100
host = '47.111.250.153'
s.connect((host,port))
print (s.recv(1024))
s.close()
