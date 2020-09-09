#!/usr/bin/python
import os
print os.getcwd()
file = open("podObs_2019-07-18T00-12-48Z.2698910.046.antPOD.rnx","r+")
str = file.read()
print str

"""
str1 = file.read(20)
print str1
position = file.tell()
print "position:",position
file.seek(0,0)
str1 = file.read(10)
print str1
"""
file.close()
os.mkdir("daichenghe")
