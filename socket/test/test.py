import os
import re
import threading
print('扫描开始')
print('请等待不要着急...........')
result=os.popen("route print").read()   #打开路由表
ip=re.search(r"0.0.0.0\s+0.0.0.0\s+\S+\s+(\S+)",result).group(1)  #选取当前上网的ip
#print(ip)
net=re.findall(r"(\d+\.\d+\.\d+\.)\d+",ip)[0]    #截取网段
#print(net)
j=[]
def task(cmd):
    r=os.popen(cmd).read()
    if "<00>" in r:
        r1=re.findall(r"(\S+.+)<00>",r)    #截取主机名和工作组
        j.append(r1)
pool=[]
for i in range(1,255):
    newip=net+str(i)
    cmd=f"nbtstat -A {newip}"   #扫描网段
    t=threading.Thread(target=task,args=(cmd,))
    pool.append(t)
    t.start()
for t in pool:
    t.join()
for i in j:
    hostname=i[0]
    workgroup=i[1]
    print(f"IP：{newip}  主机名：{hostname}  工作组：{workgroup}")
print("结束")

