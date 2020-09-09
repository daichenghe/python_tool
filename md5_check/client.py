
#!/usr/bin/env python

#_*_ encoding=utf-8 _*_

import socket,sys,os
ip_port = ('127.0.0.1',9999)
sk = socket.socket()
sk.connect(ip_port)

while True:
	input_data = input('path:')
	cmd,path = input_data.split('|')
	file_name = os.path.basename(path)
	print(file_name)
	sk.send((cmd+"|"+file_name).encode())
	send_size = 0
	Flag = True

sk.close()
