from socket import *

HOST = '<broadcast>'
PORT = 137
BUFSIZE = 1024

ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
#udpCliSock.bind((HOST, 137))
udpCliSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
start = 0
while start < 100:
	data = str('mac01\tA\t0\t11\t22\t33\t44').encode("utf-8")
	if not data:
		break
	print("sending -> %s" % data)
	udpCliSock.sendto(data, ADDR)
	import time
	time.sleep(1)
	start += 1

udpCliSock.close()


























