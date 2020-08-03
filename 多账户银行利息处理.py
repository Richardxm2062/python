# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:35:01 2017

@author: Richard祥
"""

def addtext(list,rate):
    for i in range(len(list)):
        list[i] = list[i]*(1+rate)
def main():
    list = [1000,800,600,400]
    rate = 0.1
    addtext(list,rate)
    print(list)
main()    