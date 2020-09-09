#!/usr/bin/python
# -*-coding: utf-8 -*-
import serial
import binascii
from time import sleep

f_com = open("log.txt",'w+')
f_count = open("total_count.txt",'w+')

print "set com:"
com_set = raw_input()
baud = 115200

print "start"

suc_count = 0
fail_count = 0
str1 = ''
str2 = ''
def recv(serial):
    while True:
        data = serial.read_all()
        f_com.write(data)
        return data

serial = serial.Serial(com_set,baud,timeout=0.1)
if serial.isOpen():
    print "open success"
else:
    print "open failed"
while True:
    data = recv(serial)
    #print data
    if "OpenRTK" in data:
        #f_count.write("rev")
        if "OpenRTK_wang" in data:
            suc_count += 1
            str1 += "suc_count: "
            str1 += str(suc_count)
            str1 += '\r\n'
            f_count.write(str1)
        else:
            fail_count += 1
            str2 += "fail_count: "
            str2 += str(fail_count)
            str2 += '\r\n'
            f_count.write(str2)
            print ("error!!!!!!!!!!!!!!!!!!!!")
    #sleep(5)
