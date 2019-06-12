# from time import time
# from threading import Thread 
# import requests
# requests请求
# class Download(Thread):
#     def __init__(self, url):
#         super().__init__()
#         self.url = url
#     def run(self):
#         filename = self.url[self.url.rfind('/')+1]
#         resp = requests.get(self.url)
#         with open('./__pycache__/hao'+filename,'wb') as f:
#             f.write(resp.content)
# def main():
#     resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
#     data_model = resp.json()
#     print(data_model)
#     for mm_dict in data_model['newslist']:
#         url = mm_dict['picUrl']
#         Download(url).start()

# if __name__ =="__main__":
#     main()

from socket import socket , SOCK_STREAM, AF_INET
from datetime import datetime

def main():
    # 第一步创建服务，指定使用的传输服务
    #  1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定ip和端口
    server.bind(('127.0.0.1',3000))
    # 3.开启服务
    server.listen(512)
    print('服务器开始监听在 127.0.0.1:3000')
    while True:
        # 4.通过循环接受客户端的连接并做出相应处理
        client, addr = server.accept()
        print(str(addr)+'连接到服务器')
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()

if __name__ == '__main__':
    main()
    