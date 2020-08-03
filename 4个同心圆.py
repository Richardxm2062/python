# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:31:46 2017

@author: Richard祥
"""
'''
import turtle 
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.circle(200)

turtle.penup()
turtle.goto(0,-150)
turtle.pendown()
turtle.circle(150)

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(100)

turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(50)
以上是源代码，之后用函数进行改进                   
                 '''
import turtle

def Fourcircles():
    x = 200
    for i in range(4):
        if x >=50 :
            turtle.penup()
            turtle.goto(0,-x)
            turtle.pendown()
            turtle.circle(x)
            x = x - 50
        else :
            break
Fourcircles()        