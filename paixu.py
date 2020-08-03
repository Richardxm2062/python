# -*- coding: utf-8 -*-
"""
Created on Wed May 31 23:05:25 2017

@author: Richard祥
"""
def paixu(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index-1
        while i >=0 :
            if value < list[i] :
                list[i+1] = list[i]
                list[i] = value 
                i = i - 1
            else :
                break
    print(list)        