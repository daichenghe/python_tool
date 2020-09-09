# -*- coding:utf-8 -*-
#将所有TXT连接成一个，并删除掉重复记录
import os
import time
def BianLi(rootDir):
    print "开始拼接数据，请稍等..."
    start_time = time.time()
    fh = open(./all.txt', "w")
    list1=[]
    for root,dirs,files in os.walk(rootDir):
        for filename in files:　　#这里得到的filename只是一个文件名的字符串而已，如：test.txt
            filepath = rootDir+filename　　#拼接目录和文件名得到完整路径
            file = open(filepath, 'r')　　
            for i in file:　　#i即为file中的一行，不用再readline()了
                line = str(i).strip()
                print str(line)
                if line in list1:　　#判断list里面是否有这个记录了，如果没有就加入list，如果有就跳过
                    continue
                else:
                    list1.append(line)　　#向list里添加记录
                    fh.write(line+'\n')
    fh.close()
    end_time = time.time()
    print "全部数据拼接完毕，用时%.2f秒" % (end_time - start_time)
rootDir = './'
BianLi(rootDir)　　#调用方法