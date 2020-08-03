# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 23:56:20 2017

@author: Richard祥
"""

import numpy as np 
import math 
import time 
x = np.arange(0,10000,0.01)
y = np.arange(0,10000,0.01)
z = np.arange(0,10000,0.01)
time1 = time.clock()

for i,j in enumerate(x):
    x[i] = math.pow(math.sin(j),3)

time2 = time.clock()
time_math = time2 - time1
time3 = time.clock()

for i,j in enumerate(y):
    y[i] = np.power(np.sin(j),3)    #比较单个值的循环计算

time4 = time.clock()
time_numpy1 = time4 - time3
time5 = time.clock()

z = np.power(np.sin(z),3)

time6 = time.clock()
time_numpy2 = time6 - time5 
print('利用math库遍历计算的时间为：',time_math,'\n','利用numpy库遍历计算的时间为：',time_numpy1,'\n','利用numpy库数组非遍历计算的时间为',time_numpy2)