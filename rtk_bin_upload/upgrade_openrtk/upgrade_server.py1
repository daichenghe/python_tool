import serial
import binascii
from time import sleep
import os 
import sys
import time
from socket import *

default_bios = [0xD0,0x16,0x01,0x10,0x00,0x01,0x00,0x00,0x00,0x00,\
0x00,0x00,0x20,0x45,0x50,0x46,0x41,0x45,0x46,0x45,0x4F,0x46,0x43,0x46,0x45,0x45,\
0x4C,0x43,0x41,0x43,0x41,0x43,0x41,0x43,0x41,0x43,0x41,0x43,0x41,0x43,0x41,0x43,\
0x41,0x41,0x41,0x00,0x00,0x20,0x00,0x01,0x8C,0xA4,0xD2,0x03,0x9F,0xBF,0x48,0x31,\
0x9C,0xF3,0x34,0xE6]


def net_bios():
    s = socket(AF_INET, SOCK_DGRAM)
    s.setblocking(False)
    try:
        s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        print('connect')
    except:
        pass
    PORT = 137
    network = '<broadcast>'
    # 发送数据:
    #s.sendto(u"test123456789".encode("utf-8"), (network, PORT))
    buf_size = 1024
    data_rev = ''
    while True:
        s.sendto(bytes(default_bios), ('192.168.137.255', PORT))
        try:
            data_rev, ADDR = s.recvfrom(buf_size)
            print(len(data_rev))
            print(int(data_rev[len(data_rev) - 1]))
            break
        except:
            time.sleep(1)
            print('wait udp')
        print("get：", data_rev)
    s.close()
    return True

#com_set = raw_input()
#com_set = input()
select = '1'
#BAUD = '57600'
BAUD = '115200'
baud = int(BAUD)
file_name = 'compare.bin'
file = open(file_name,"wb")



#binfile = open("rtk.bin", 'rb')
#size = os.path.getsize("rtk.bin") 
print ("set your file:")
#bin_file = input()
bin_file = 'firmware.bin'
binfile = open(bin_file, 'rb')
size = os.path.getsize(bin_file) 
all_bytes_len = size
fs_len = size
boot_mode = 0
print ("size:%d" % size)
#serial = serial.Serial(com_set, baud, timeout=0.1)  #/dev/ttyUSB0

def calc_crc(payload):
	'''Calculates CRC per 380 manual
	'''
	crc = 0x1D0F
	for bytedata in payload:
		crc = crc^(bytedata << 8) 
		for i in range(0,8):
			if crc&0x8000:
				crc = (crc << 1)^0x1021
			else:
				crc = crc << 1

	crc = crc & 0xffff
	return crc


def get_remote_machine_info():  
	remote_host = 'OPENRTK'  
	try:
		print("IP address of %s: %s" % (remote_host, gethostbyname(remote_host)))
		return True
	except error as err_msg:
		print("%s: %s" % (remote_host, err_msg))
		return False

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
	
	
def start_bootloader(conn):
	'''Starts bootloader
		:returns:
			True if bootloader mode entered, False if failed
	'''
	print ("start")
	C = [0x55, 0x55, ord('J'), ord('I'), 0x00 ]
	crc = calc_crc(C[2:4] + [0x00])    # for some reason must add a payload byte to get correct CRC
	crc_msb = (crc & 0xFF00) >> 8
	crc_lsb = (crc & 0x00FF)
	C.insert(len(C), crc_msb)
	C.insert(len(C), crc_lsb)
	'''
	serial.write([0x01,0x02])
	sleep(2)
	'''
	conn.send(bytes(C))
	print (C)
	#time.sleep(2)   # must wait for boot loader to be ready
	#R = serial.read(5)
	R = conn.recv(7)
	print(R)
	if R[0] == 85 and R[1] == 85:
		#packet_type =  '{0:1c}'.format(R[2]) + '{0:1c}'.format(R[3])
		packet_type = R[2] + R[3]
		if packet_type == 'JI':
			conn.recv(R[4]+2)
			print('bootloader ready')
			time.sleep(2)
			if boot_mode == 0:
				print('resync with device')
				time.sleep(2)
			return True
		else: 
			return False
	else:
		return False



def start_app(conn):
	'''Starts app
	'''
	C = [0x55, 0x55, ord('J'), ord('A'), 0x00 ]
	crc = calc_crc(C[2:4] + [0x00])    # for some reason must add a payload byte to get correct CRC
	crc_msb = (crc & 0xFF00) >> 8
	crc_lsb = (crc & 0x00FF)
	C.insert(len(C), crc_msb)
	C.insert(len(C), crc_lsb)
	conn.send(bytes(C))
	sleep(2)
	print (C)
	R = conn.recv(1024)   #7
	'''
	if (R[0]) == 85 and (R[1]) == 85:
		packet_type =  R[2] + R[3]
		print(packet_type)
	'''
	if R[0] == 85 and R[1] == 85:
		packet_type = '{0:1c}'.format(R[2]) + '{0:1c}'.format(R[3])
		print(packet_type)

def write_block(conn_tcp,buf, data_len, addr):
	'''Executed WA command to write a block of new app code into memory
	'''
	print(data_len, addr)
	C = [0x55, 0x55, ord('W'), ord('A'), data_len+5]
	addr_3 = (addr & 0xFF000000) >> 24
	addr_2 = (addr & 0x00FF0000) >> 16
	addr_1 = (addr & 0x0000FF00) >> 8
	addr_0 = (addr & 0x000000FF)
	C.insert(len(C), addr_3)
	C.insert(len(C), addr_2)
	C.insert(len(C), addr_1)
	C.insert(len(C), addr_0)
	C.insert(len(C), data_len)
	for i in range(data_len):
		#C.insert(len(C), ord(buf[i]))
		C.insert(len(C), buf[i])
	crc = calc_crc(C[2:C[4]+5])  
	crc_msb = int((crc & 0xFF00) >> 8)
	crc_lsb = int((crc & 0x00FF))
	C.insert(len(C), crc_msb)
	C.insert(len(C), crc_lsb)
	status = 0
	while (status == 0):
		print('-------------------------------------')
		print(bytes(C))
		conn_tcp.send(bytes(C))
		test = []
		for ele in C:
			test.insert(len(test),hex(ele))
		print ("upload progress: %.3f%%" % (float(addr)/float(fs_len)*100))
		if addr == 0:
		   sleep(10)
		else:
		   #sleep(0.01)
		   sleep(0.02)

		print('wait')
		#input()
		R = conn_tcp.recv(12)  #longer response
		response=[]
		for ele in bytearray(R):
			response.append(ele)
		print(response)
		status = 1
		if len(R) > 1 and (R[0]) == 85 and (R[1]) == 85:
			packet_type = '{0:1c}'.format(
				R[2]) + '{0:1c}'.format(R[3])
			if packet_type == 'WA':
				status = 1
			else:
				print('error')
				sys.exit()
				status = 0
		else:
			print(len(R))
			print(R)
			sleep(1)
			print('no packet')
			sys.exit()
		


def recv(serial):
	while True:
		if select == "2":
			data = binascii.b2a_hex(serial.read_all())
			file.write(data)
			#data = serial.read_all()
			#data = "test"
		else:
			#data = binascii.b2a_hex(serial.read_all())
			data = serial.read_all()
			file.write(data)
		'''
		if data == '':
			continue
		else:
			break
		'''
		#sleep(0.02)
	return data

write_flag = 1
send_count = 0
max_data_len = 200
write_len = 0
#start_app()

def connect_client():
    test_count = 0
    '''
    while get_remote_machine_info() == False:
        time.sleep(1)
    while test_count < 30:
        get_remote_machine_info()
        time.sleep(1)
        test_count+= 1
    ''' 
    net_bios()
    time.sleep(1)
    #get_remote_machine_info()
    #time.sleep(5)
    hostIp='192.168.137.1'
    port=2203
    sock=socket(AF_INET,SOCK_STREAM)

    sock.bind((hostIp,port))
    sock.listen(5)
    print ('start listen {0}:{1}'.format(hostIp,port))
    conn,addr = sock.accept()
    print ('recived a client from {0}'.format(addr))
    while True:
        recivedData=conn.recv(1024)
        conn.send('i am pc {0}'.format(recivedData.decode()).encode())
        print ('get data: {0}'.format(recivedData.decode()))
        if('openrtk' in recivedData.decode()):
            print('get openrtk message')	
            break
    return conn
		
if __name__ == '__main__':

    conn = connect_client()
    start_bootloader(conn)

    sleep(6)
    conn.close()
    sleep(10)
    print('start write app')

    conn = connect_client()
    serial.baud = 115200
    while (write_len < fs_len):
        print('start flash')
        data_to_write = binfile.read(max_data_len)
        #packet_data_len = max_data_len 
        if (fs_len - write_len) > max_data_len:
            packet_data_len = max_data_len 
        else:
            packet_data_len = fs_len - write_len
        write_block(conn,data_to_write,packet_data_len, write_len)
        #def write_block(conn,buf, data_len, addr):
        '''111'''
            

        '''222'''
        write_len += packet_data_len
    print ("upload progress: %.3f%%" % 100)
    print ("start app")
    sleep(5)
    start_app(conn)
        #test = raw_input()
    print ('end')
    conn.close()
        #serial.write(data) 

