#!/usr/bin/python
#!coding:utf-8

from socket import *
import os,sys
import time

def get_remote_machine_info():  
	remote_host = 'OPENRTK'  
	try:
		print("IP address of %s: %s" % (remote_host, gethostbyname(remote_host)))
		return True
	except error as err_msg:
		print("%s: %s" % (remote_host, err_msg))
		return False


C = [0x55, 0x55, ord('g'), ord('V'), 0x00 ,171,238]
test = (bytes(C))	
print(test)


if __name__=="__main__":
	#hostIp='127.0.0.1'
	while get_remote_machine_info() == False:
		time.sleep(1)
	time.sleep(5)
	hostIp='192.168.137.1'
	port=2203
	sock=socket(AF_INET,SOCK_STREAM)
	sock.bind((hostIp,port))
	sock.listen(5)
	print ('start listen {0}:{1}'.format(hostIp,port))
	while True:
		conn,addr = sock.accept()
		print ('recived a client from {0}'.format(addr))
		while True:
			recivedData=conn.recv(1024)
			if not recivedData:
				print ('close...')
				break
			conn.send('i am pc {0}'.format(recivedData.decode()).encode())
			print ('get data: {0}'.format(recivedData.decode()))
			if('openrtk' in recivedData.decode()):
				print('get openrtk message')
			C = [0x55, 0x55, ord('g'), ord('V'), 0x00 ,171,238]
			conn.send(bytes(C))		
			time.sleep(1)			
		conn.close()