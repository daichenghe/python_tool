#!/usr/bin/python

import os


if __name__ == '__main__':
	cmd = "TeseoProgrammer_v2.9.0.exe program -f t5 -i sta.bin -o log.txt -c com53 -b 230400 -m SQI -d 0x10000400 -e TRUE -r TRUE";
	print ("cmd = %s" % cmd);

	os.system(cmd)
