data = [0x55, 0x55, 0x70, 0x53, 0x7C, 0x4A, 0x08, 0x00, 0x00, 0x00, \
		0x00, 0x00, 0x00, 0x58, 0xC2, 0x07, 0x41, 0x01, 0x00, 0x00, \
		0x00, 0x41, 0xAC, 0x9F, 0x9A, 0x25, 0x82, 0x3F, 0x40, 0x07, \
		0x55, 0x89, 0x50, 0xB0, 0x19, 0x5E, 0x40, 0x00, 0x00, 0x58, \
		0xCF, 0xCC, 0x0C, 0x3C, 0x40, 0x1C, 0x00, 0x00, 0x00, 0x9A, \
		0x99, 0x19, 0x3F, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, \
		0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0A, \
		0xD7, 0xA3, 0x3C, 0x00, 0x00, 0x20, 0x21, 0x0A, 0xD7, 0x23, \
		0x3C, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, \
		0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, \
		0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, \
		0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, \
		0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xDD, 0xE5]

ori_data = input('data to save:\r\n')

valid_data = ori_data.split(' ')
#print(valid_data)


fs = open('save.bin','wb')
'''
fs.write(bytes(data))
'''
bin_data = []
for ele in valid_data:
	ele_to_write = (int(ele,16))
	bin_data.append(ele_to_write)
	print(ele_to_write)
	#print(ele)
fs.write(bytes(bin_data))
