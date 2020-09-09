import socket


def get_remote_machine_info():  # 定义get_remote_machine_info()函数
    remote_host = 'TEST_OPENRTK'  # 定义远程设备名称
    try:  # try-except块
        print("IP address of %s: %s" % (remote_host, socket.gethostbyname(remote_host)))
        # 打印远端设备名称及对应的IP地址
    except socket.error as err_msg:    # 如果IP地址没有获取成功,则打印对应的错误消息
        print("%s: %s" % (remote_host, err_msg))


if __name__ == '__main__':
    get_remote_machine_info()