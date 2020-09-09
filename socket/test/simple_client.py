
import socket

 


def get_openrtk_ip():  
    remote_host = 'OPENRTK'  
    try:  
        print("IP address of %s: %s" % (remote_host, socket.gethostbyname(remote_host)))
        return socket.gethostbyname(remote_host)
    except socket.error as err_msg:
        print("%s: %s" % (remote_host, err_msg)) 

remote_ip = get_openrtk_ip()
print(remote_ip)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((remote_ip,8088))

while True:

	info = client.recv(1024)

	print("server：",info)	
	data = input("put")
	client.send(data.encode("utf-8"))



 
