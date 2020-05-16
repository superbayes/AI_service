#!/usr/bin/env python
# coding=utf-8
import socketserver
import threading

def model_predict(data):
    """
    在这里处理你的模型预测,业务逻辑
    :param data:
    :return:
    """
    data = data +  '----机器学习的模型在这里处理数据,返回结果......'
    return data


class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print ('running')
        while True:
            try:
                data = self.request.recv(1024).strip().decode('utf-8')
                print("收到数据: ", data)
                if data =='exit' or data == 'quit':
                    self.server.shutdown()
                    self.request.close()
                    break
                else:
                    # fixme 处理数据
                    data2 = model_predict(data)
                    # todo 将最终结果返回
                    self.request.sendall(data2.encode('utf-8'))
            except Exception as e:
                self.server.shutdown()
                self.request.close()
                break
class start_server():
    def __init__(self,host="localhost",port=9999):
        self.host=host
        self.port=port
    def start_socketserver(self,RequestHandler):
        server = socketserver.ThreadingTCPServer((self.host, self.port), RequestHandler)
        s = threading.Thread(target=server.serve_forever())
        s.start()
if __name__ == "__main__":
    start_server(host="localhost",port=9999).start_socketserver(RequestHandler)

