
#!/usr/bin/env python

# -*- coding: utf-8 -*-

 

"""

    当我们运行该程序时因为 while True 所以会持续的运行. 

    这里监听的是 SIGTERM 信号, 所以当我们在终端输入 kill pid (linux kill

    默认是发送SIGTERM)时, 

    程序就会输出: 收到信号 15 <frame object at 0x7ff695738050> 0

    当超过3次时就强制把自己杀死.

    所以 SIGTERM 很适合用来做一些清理的工作

"""

 

import sys



import time

import os

import signal

 

receive_times = 0

 

def handler(signalnum, frame):

    global receive_times

    print (u"收到信号", signalnum, frame, receive_times)

    receive_times += 1

    if receive_times > 3:

        exit(0) # 自己走

 

def main():

    print ("pid:", os.getpid())

    signal.signal(signal.SIGINT, handler)

    while True:
        pass

 

if __name__ == '__main__':

    main()


