import os
import time
import sys


	
def file_combine(file_boot,file_app,file_all):
	fs_boot = open(file_boot,'rb')
	fs_app = open(file_app,'rb')
	fs_all = open(file_all,'wb')
	boot_data = fs_boot.read()
	boot_extra_data = []
	app_data = fs_app.read()
	boot_size = os.path.getsize(file_boot)
	app_size = os.path.getsize(file_app)
	fs_all.write(boot_data)
	extra_data_len = 0x10000 - boot_size
	print(extra_data_len)
	for i in range(extra_data_len):
		boot_extra_data.append(0xff)
	print(len(boot_extra_data))
	fs_all.write(bytes(boot_extra_data))	
	fs_all.write(app_data)	
	
if __name__ == '__main__':
	print(sys.argv[1])
	print(sys.argv[2])
	print(sys.argv[3])
	file_combine(sys.argv[1],sys.argv[2],sys.argv[3])

	

	
	