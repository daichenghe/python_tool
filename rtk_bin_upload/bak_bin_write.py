import serial
import binascii
from time import sleep
import os 

print "out your com:"
com_set = raw_input()
print "1:ascii 2:hex" 
print "select"
select = '1'
#print select

print "baud:"

BAUD = '460800'
baud = int(BAUD)

print "file name:"
file_name = '111'
file = open(file_name,"wb")

binfile = open("rtk.bin", 'rb')
size = os.path.getsize("rtk.bin") 
all_bytes_len = size
print "size:%d" % size
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
if __name__ == '__main__':
	serial = serial.Serial(com_set, baud, timeout=0.1)  #/dev/ttyUSB0
	if serial.isOpen() :
		print("open success")
	else :
		print("open failed")

	while write_flag > 0:
		#data = recv(serial)
		#print data1
		data_to_write = binfile.read(10)
		serial.write(data_to_write)
		all_bytes_len -= 10
		send_count += 10
		if(all_bytes_len) < 10:
			data_to_write = binfile.read(all_bytes_len - 1)
			serial.write(data_to_write)
			write_flag = 0
			print send_count
			break
		sleep(0.08)
		#print(data)
		#print("receive : ",data)
		#print(data)
	print 'end'
		#serial.write(data) 
