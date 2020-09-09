# -*- coding:utf-8 -*-
import os
import time
str_all = ''
print ('test')
fs_ave = ''
def replace(rootDir):
    global str_all
    print ("start...")
    print ("file name")
    #file_in = raw_input()
    file_in = "tes.txt"
    fh = open(file_in, "r")
    str = fh.read()
    ret = str.split(',')
    for ele in ret:
        #print ele
        ret_ocd = int(ele, 16)
        asc_to_str = chr(ret_ocd)
        #print asc_to_str
        str_all = str_all + asc_to_str
        #asc_to_str = chr(int(inter))
        #print ret
    fh.close()
    print (str_all)
    fs_save = open("html_save.txt", "w")
    fs_save.write(str_all)
    fs_save.close
    print ("end...")
	
replace('./')
