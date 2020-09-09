#!/usr/bin/python
#!coding:utf-8

from socket import *
import os,sys
import time
import psutil

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


def get_host_ip():
	try:
		s = socket(AF_INET, SOCK_DGRAM)
		s.connect(('8.8.8.8', 80))
		test = s.getsockname()
		print(test)
		ip = s.getsockname()[0]
	finally:
		s.close()

	return ip


def get_netcard():
	"""获取网卡名称和ip地址
	"""
	netcard_info = []
	info = psutil.net_if_addrs()
	#print(info.items())
	for k, v in info.items():
		for item in v:
			if item[0] == 2 and not item[1] == '127.0.0.1' :
				print(type(item))
				print(item)
				print(item[0])
				print(item[1])
				#去除通过dhcp获取ip方式没获取时分配的的自动专有地址
				if "169.254."not in item[1]:
					# netcard_info.append((k, item[1]))
					netcard_info.append(item[1])
		#print("K",k)
	return netcard_info

if __name__=="__main__":
    print(get_netcard())
    input()
    while get_remote_machine_info() == False:
        time.sleep(1)
    time.sleep(1)
    #hostIp = get_host_ip()
    hostIp='192.168.137.2'
    #hostIp = '10.0.20.157'
    port=2203
    sock=socket(AF_INET,SOCK_STREAM)
    sock.setblocking(False)
    sock.bind((hostIp,port))
    #sock.setblocking(False)
    sock.listen(5)
    print ('start listen {0}:{1}'.format(hostIp,port))
    while True:
        try:
            conn,addr = sock.accept()
            break
        except:
            print('wait')
            time.sleep(1)
    print ('recived a client from {0}'.format(addr))
    while True:
        try:
            recivedData=conn.recv(1024)
        except:
            time.sleep(1)
            print('wait')
        conn.send('i am pc'.encode())
        print (recivedData)
        if('openrtk' in recivedData.decode()):
            print('get openrtk message')	
            break
    while True:
            '''
            C = [0x55, 0x55, ord('g'), ord('V'), 0x00 ,171,238]
            conn.send(bytes(C))		
            '''
            gv_cmd = packet_cmd('pG')
            conn.send(gv_cmd)
            try:
                recivedData=conn.recv(1024)
            except:
                pass
            if not recivedData:
                print ('close...')
            print (bytes(recivedData))
            #print ('get data: {0}'.format(recivedData.decode()))
            time.sleep(0.1)			
    conn.close()
