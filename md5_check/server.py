
#!/usr/bin/env python

# _*_ encoding=utf-8 _*_

 

import socketserver,os
import hashlib
import serial
import MySQLdb
 

class MyServer(socketserver.BaseRequestHandler):
	def handle(self):
		conn = self.request
		print('connected...')
		while True:
			pre_data = conn.recv(1024).decode()
			cmd,sql_cmd = pre_data.split('|')
			recv_size = 0
			Flag = True
			'''
			while Flag:
				if int(cmd_size)>recv_size:
					data = conn.recv(1024)
					cmd_size += len(data)
				else:
					recv_size = 0
					Flag = False
					continue
			'''
			db = MySQLdb.connect("localhost", "root", "dch19901231", "openrtk", charset='utf8' )
			cursor = db.cursor()
			cursor.execute(sql_cmd)
			results = cursor.fetchall()
			db.commit()
			db.close()
			print('write sql success')

            

instance = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyServer)            
instance.serve_forever()
