# -*- coding:utf-8 -*-
import os
import time
str_all = ''
print 'test'
while 1:
    global str_all
    print "start..."
    print "put ascii:"
    str = raw_input()
    str = str.replace(' ','')
    ret = str.split(',')
    for ele in ret:
        #print ele
        #if(ele.isdigit()):
        if 1:
            ret_ocd = int(ele, 16)
            asc_to_str = chr(ret_ocd)
        #print asc_to_str
            str_all = str_all + asc_to_str
        #asc_to_str = chr(int(inter))
        #print ret
    print str_all
    str_all = ''
