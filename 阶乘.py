# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:32:10 2017

@author: Richard祥
"""

def jiecheng(x):
    if x ==0:
        return 1
        
    else:
        return jiecheng(x-1)*x
def main():
    m = eval(input('Enter the number :'))
    y = jiecheng(m)
    print(y)             
