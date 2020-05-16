import socket
def send_exit():
    ser = socket.socket()
    ser.connect(('127.0.0.1', 12345))  # 12348
    ser.sendall(b'exit')
    ser.close()

def send_text(data=''):
    ser = socket.socket()
    ser.getsockname()
    ser.connect(('127.0.0.1', 12345))  # 12348
    ser.sendall(data.encode('utf-8'))


if __name__ == '__main__':
    data = '最近要处理socket并发，发现Python提供的SocketServer很好用，于是我自己试了下。废话不多说，先上一波代码'
    ser = socket.socket()
    ser.connect(('127.0.0.1', 9999))
    print(ser.getsockname())
    while data:
        ser.sendall(data.encode('utf-8'))
        data = ser.recv(2048)
        print("收到: ",data.decode('utf-8').strip())
        data = input("输入发送的信息: ")

    ser.close()
