# udp广播案例
from socket import *
s=socket(AF_INET,SOCK_DGRAM)
# 设置套接字
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)
# 选择一个接收地址
s.bind(('0.0.0.0',137))
while True:
    try:
        msg,addr=s.recvfrom(1024)
        print('from %s bg %s'% (addr,msg.decode()))
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
s.close()