import os
import sys

if __name__ == "__main__":
	if len(sys.argv) > 2:
		print('failed,exit')
	bin_file = sys.argv[1]
	print(bin_file)
	cmd = ".\openocd.exe -f .\stlink.cfg -f ./stm32f4x.cfg -c \"program %s 0x08000000\" -c \"reset run\" -c \"shutdown\"" % bin_file
	print(cmd)
	os.system(cmd)