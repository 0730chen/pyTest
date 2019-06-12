# import serial
# serialPort = 'com1'
# baudRate = 9600
# ser = serial.Serial(serialPort,baudRate,timeout=0.5)
# print(serialPort,baudRate)
# # ser = serial.Serial(port='com1', baudrate=9600)
# # print(ser.portstr)
# # def serial_communi(ser,msg):
# #      n = ser.write(msg.encode())
# #      print(n)
# #      s = ser.read(n)
# #      print(s)
# #       # n is the length of msg sent
# # #  n = ser.write(msg.encode())
# #     #  print(n)
# # #   s = ser.read(n)
# # serial_communi(ser,'sss')
# while 1:
#     str = ser.readline()
#     print(str)
# ser.close()
# import day1 as foo1
# import day2 as foo2

# print(foo1.foo())
from math import sqrt

class Point(object):
    def __init__(self ,x=0 ,y=0):
        '''初始化方法'''
        self.x = x
        self.y = y
    def mov(self,x, y):
        self.x = x
        self.y = y
    def addmve(self,addx,addy):
        self.x +=addx
        self.y +=addy
    def distan_to(self,tox):
        dx = self.x - tox.x
        dy = self.y - tox.y
        return sqrt(dx ** 2 + dy ** 2)
    def __self__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))
def main():
    p1 = Point(3,5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.mov(2,3)
    print(p2)
    print(p1.distan_to(p2))

if __name__ == '__main__':
    main()


