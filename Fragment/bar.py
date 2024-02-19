# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 00:18:30 2018

@author: Richa
"""
import time 
scale = 10
for i in range(scale+1):
    a = '*'*i
    b = '.'*(scale-i)
    c = 10*i
    print('\r {0:^3.0f}%   [{1}->{2}]'.format(c,a,b),end='') #\r将指针回到单行头部，end=''表示不跳行
    time.sleep(0.5) #挂起程序
    