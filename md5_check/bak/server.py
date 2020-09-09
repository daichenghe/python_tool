
#!/usr/bin/env python

# _*_ encoding=utf-8 _*_

 

import socketserver,os

 

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):

        base_path = 'D:\资料\工具\python\md5_check\test'

        conn = self.request

        print('connected...')

        while True:

            pre_data = conn.recv(1024).decode()

            #获取请求方法，文件名，文件大小

            cmd,file_name,file_size = pre_data.split('|')

            #已经接收文件的大小

            recv_size = 0

            #上传文件路径拼接

            file_dir = os.path.join(base_path,file_name)

            f = open('456.txt','wb')

            Flag = True

            while Flag:

                #未上传完毕

                if int(file_size)>recv_size:

                    data = conn.recv(1024)

                    recv_size += len(data)

                else:

                    recv_size = 0

                    Flag = False

                    continue

                #写入文件

                f.write(data)

            print('upload successed')

            f.close()

            

instance = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyServer)            

instance.serve_forever()
