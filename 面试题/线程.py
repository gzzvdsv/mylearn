#!/usr/bin/python3
# _thread函数已经不在使用了    但是py有两种调用多线程的方法一个是  _thread  函数  另一个是  threading 类调用方法
# 函数式 调用 _thread.start_new_thread()

import _thread
import time
# _thread.start_new_thread()
# 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
def print_time(threadName,delay):
   count=0
   while count<5:
       time.sleep(delay)
       count+=1
       print("%s:%s"%(threadName,time.ctime(time.time())))
# 创建两个线程
try:
    _thread.start_new_thread(print_time,("Thread-2",4))
    _thread.start_new_thread(print_time,("Thread-1",2,))
except:
    print('Error:无法启动线程')
while 1:
   pass