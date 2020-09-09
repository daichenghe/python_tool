# -*- coding:utf-8 -*-
f = open("aceinna.png","rb")
f.seek(0,0)  
fs = open("png.txt","w")
index=0  
for i in range(0,16):  
    print "%3s" % hex(i) ,  
print  
for i in range(0,16):  
    print "%-3s" % "#" ,  
print  
while True:  
    temp=f.read(1)  
    if len(temp) == 0:  
        break  
    else:  
        to_write = 	temp.encode('hex')
        print "%3s" % to_write,  
        index=index+1  
        fs.write(to_write)
    if index == 16:  
        index=0  
        fs.write("\n")
        print   
f.close()
fs.close