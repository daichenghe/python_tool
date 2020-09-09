#!/usr/bin/python
#!coding:utf-8

from socket import *
import os,sys

if __name__ == "__main__":
    #hostIp='192.168.137.1'
    hostIp = "192.168.137.63"
    port=2202
    sock=socket(AF_INET,SOCK_STREAM)
    messages=['hello I am a client']
    messages=messages+sys.argv[1:]
    sock.connect((hostIp,port))
    print ('[info]    已经连接到server ')
    
    for message in messages:
        sock.send(message.encode())
        print (sock.recv(1024).decode())
    sock.close()
