import socket               
s = socket.socket()         
host = socket.gethostname() 
print(host)
port = 2202                
s.bind((host, port))        

s.listen(5)                 
c,addr = s.accept()     
print ('connect: ', addr)
c.send(b"hello world!")
c.close()                
