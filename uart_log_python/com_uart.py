import serial
import binascii
from time import sleep

print ("out your com:")
com_set = input()
print ("1:ascii 2:hex")
print ("select")
select = input()
#print select

print ("baud:")

BAUD = input()
baud = int(BAUD)

print ("file name:")
file_name = input()
file = open(file_name,"wb")
def recv(serial):
    while True:
        if select == "2":
            data = binascii.b2a_hex(serial.read_all())
            file.write(data)
            #data = serial.read_all()
            #data = "test"
        else:
            #data = binascii.b2a_hex(serial.read_all())
            data = serial.read_all()
            file.write(data)
        '''
        if data == '':
            continue
        else:
            break
        '''
        #sleep(0.02)
    return data

if __name__ == '__main__':
    serial = serial.Serial(com_set, baud, timeout=0.1)  #/dev/ttyUSB0
    if serial.isOpen() :
        print("open success")
    else :
        print("open failed")

    #while True:
    data = recv(serial)
        
        #print (data1)
        #print(data)
        #print("receive : ",data)
        #print(data)

        #serial.write(data) 
