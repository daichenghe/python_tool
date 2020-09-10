import os
import time
import sys


def get_list_from_int(value):
	value_list = [0 for x in range(0, 4)]
	value_list[0] = value & 0xff
	value_list[1] = (value >> 8) & 0xff
	value_list[2] = (value >> 16) & 0xff
	value_list[3] = (value >> 24) & 0xff
	return value_list
	
def file_combine(file_rtk,file_sdk,file_all):
	fs_rtk = open(file_rtk,'rb')
	fs_sdk = open(file_sdk,'rb')
	fs_all = open(file_all,'wb')
	rtk_size = os.path.getsize(file_rtk)
	sdk_size = os.path.getsize(file_sdk)
	rtk_data = fs_rtk.read()
	sdk_data = fs_sdk.read()

	rtk_size_list = []
	rtk_size_list = get_list_from_int(rtk_size)
	sdk_size_list = []
	sdk_size_list = get_list_from_int(sdk_size)
	fs_all.write(b'rtk_start:')
	fs_all.write(bytes(rtk_size_list))
	fs_all.write(rtk_data)
	fs_all.write(b'sdk_start:')
	fs_all.write(bytes(sdk_size_list))
	fs_all.write(sdk_data)	
	
if __name__ == '__main__':
	print(sys.argv[1])
	print(sys.argv[2])
	print(sys.argv[3])
	file_combine(sys.argv[1],sys.argv[2],sys.argv[3])

	

	
	