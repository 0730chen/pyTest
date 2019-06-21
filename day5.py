# # import time 
# # import shutil
# # import os

# # # seconds = time.time()
# # # # print(seconds)
# # # localtime = time.localtime(seconds)
# # # # print(localtime)
# # # asctime = time.asctime(localtime)
# # # # print(asctime)格式化输出时间

# # # shutil.copy('./hello.py','./day2.py')
# # # os.system('1s -l')
# # # os.chdir('./__pycache__')
# # # os.system('1s -l')
# # # os.mkdir('hao')
# # def dist():
# #     stu = {'name':'落尘','age':'12','wife':'琉璃'}
# #     print(stu)
# #     print(stu.keys())
# #     print(stu.values())
# #     print(stu.items())
# #     for i in stu.items():
# #         print(i)
# #         print('我在循环中')
# #         print(i[0],i[1])
    


# # if __name__ == '__main__':
# #     dist()

# from abc import ABCMeta,abstractclassmethod
# from math import pi 使用抽象类继承

# class Shape(object,metaclass = ABCMeta):
#     @abstractclassmethod
#     def perimeter(self):
#         pass
#     @abstractclassmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self._radius = radius
#     def perimeter(self):
#         return 2 *pi*self._radius
#     def area(self):
#         return pi*self._radius**2

#     def __str__(self):
#         return '我是圆圈'

# class Rect(Shape):
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#     def perimeter(self):
#         return 2*(self._height + self._width)
#     def area(self):
#         return self._height * self._width
#     def __str__(self):
#         return '我是一个矩形'
# if __name__ == '__main__':
#     shape = [Circle(5),Circle(3.2), Rect(3.2,6.3)]

#     for i in shape:
#         print(i)
#         print('周长',i.perimeter())

from socket import socket
#  自定义线程类
from threading import Thread
def main():
    class Refresh(Thread):
        def __init__(self,client):
            super().__init__()
            self._client = client
        def run(self):
            while running:
                data = self._client.recv(1024)
                print(data.decode('utf-8'))
