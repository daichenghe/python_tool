# UDP广播案例
from socket import *
from time import sleep
# 设定目标地址
dest=('<broadcast>',137)

#dest=('192.168.137.1',137)

s=socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
data = input('>')
while True:
    sleep(2)
    s.sendto(data.encode('utf-8'), dest)
s.close()