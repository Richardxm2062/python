# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 01:08:49 2018

@author: Richa
"""

from turtle import*
x = 200

for i in range(200):
    if x > 0:
        seth(90)
        fd(x)
        seth(0)
        fd(x)
        x-=5
        seth(-90)
        fd(x)
        seth(-180)
        fd(x)
        x-=5
    else:
        done() #防止窗口死掉