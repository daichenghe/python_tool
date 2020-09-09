import binascii
import struct
import os

#fs = open("rtk.bin","rb")
fs = open("hex_str.txt",'w')

binfile = open("rtk.bin", 'rb')
size = os.path.getsize("rtk.bin") 
count = 0;
for i in range(size):
	data = binfile.read(1) 
	ret = binascii.b2a_hex(data)
	str_hex = '0x' + ret
	
	fs.write(str_hex)
	fs.write(',')
	count += 1
	if count > 16:
		fs.write('\r\n')
		count = 0
	#print(str_hex)
binfile.close()
