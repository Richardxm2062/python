# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 01:08:49 2018

@author: Richa
"""
import turtle 

x = 200

for i in range(200):
    if x > 0:
        turtle.setheading(90)
        turtle.forward(x)
        turtle.setheading(0)
        turtle.forward(x)
        x -= 5
        turtle.setheading(-90)
        turtle.forward(x)
        turtle.setheading(-180)
        turtle.forward(x)
        x -= 5
    else:
        turtle.done() # 防止窗口死掉
