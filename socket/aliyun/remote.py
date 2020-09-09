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






if __name__=="__main__":
	#hostIp='127.0.0.1'
	while get_remote_machine_info() == False:
		time.sleep(1)