#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import thread
import time
 
# 为线程定义一个函数
def print_time( threadName, delay):
   while True:
		print "hello\r\n"
		time.sleep(0.6)
# 创建两个线程
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   #thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"
 
while 1:
   pass