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
    print('\r {0:^3.0f}%   [{1}->{2}]'.format(c,a,b),end='')
    time.sleep(0.5)
    