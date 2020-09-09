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



def calc_crc(payload):
    '''
    Calculates 16-bit CRC-CCITT
    '''
    crc = 0x1D0F
    for bytedata in payload:
        crc = crc ^ (bytedata << 8)
        i = 0
        while i < 8:
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc = crc << 1
            i += 1

    crc = crc & 0xffff
    crc_msb = (crc & 0xFF00) >> 8
    crc_lsb = (crc & 0x00FF)
    return [crc_msb, crc_lsb]


def packet_cmd(cmd):
	packet = []
	#packet.extend(bytearray(cmd, 'utf-8'))
	packet.extend(bytes(cmd, 'utf-8'))
	#print(packet)
	msg_len = 0
	packet.append(msg_len)
	final_packet = packet
	# print(message_type, final_packet)
	cmd_packet = [0x55,0x55] + final_packet + calc_crc(final_packet)
	return bytes(cmd_packet)


'''
test_str = 'gV'
cmd_packet = packet_cmd(test_str)
print(cmd_packet)
'''


if __name__=="__main__":
	#hostIp='127.0.0.1'
	while get_remote_machine_info() == False:
		time.sleep(1)
	time.sleep(1)
	hostIp='192.168.137.1'
	port=2204
	sock=socket(AF_INET,SOCK_STREAM)
	sock.bind((hostIp,port))
	sock.listen(5)
	print ('start listen {0}:{1}'.format(hostIp,port))
	conn,addr = sock.accept()
	print ('recived a client from {0}'.format(addr))
	fs = open("log.txt","wb")
	while True:
		recivedData=conn.recv(1024)
		#conn.send('i am pc'.encode())
		print (recivedData)
		conn.send('get configuration\r\n'.encode())
		recivedData=conn.recv(1024)
		print (recivedData)
		if('openrtk' in recivedData.decode()):
			print('get openrtk message')	
			time.sleep(1)	
			conn.send('log debug on\r\n'.encode())
			break

	while True:
			recivedData=conn.recv(1024)
			fs.write(recivedData)
			#print (bytes(recivedData))
			#print ('get data: {0}'.format(recivedData.decode()))
			#time.sleep(0.1)			
	conn.close()