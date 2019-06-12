# import asyncio
# import threading


# # 通过async修饰的函数不再是普通函数而是一个协程
# # 注意async和await将在Python 3.7中作为关键字出现
# async def hello():
#     print('%s: hello, world!' % threading.current_thread())
#     await asyncio.sleep(2)
#     print('%s: goodbye, world!' % threading.current_thread())


# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# # 等待两个异步I/O操作执行结束
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()\
#使用yield实现生成器
# def fib(num):
#     n, a, b = 0,0,1
#     while n <num :
#         yield b
#         a, b = b, a+b
#         n +=1
# for x in fib(20):
#     print(x)

import multiprocessing
import os

def sub_tasks(queue):
    print('子进程:',os.getpid())
    counter = 0
    while counter < 1000:
        queue.put('Pong')
        counter +=1
if __name__ == '__main__':
    print('当前进程',os.getpid())
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target = sub_tasks, args=(queue,))
    p.start()
    counter = 0
    while counter < 1000:
        queue.put('Ping')
        counter +=1
    p.join()
    print('子任务完成')
    for _ in range(2000):
        print(queue.get(),end='')
