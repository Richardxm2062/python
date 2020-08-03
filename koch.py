# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:54:04 2018

@author: Richa
"""
import turtle
def koch(size,n):
    if n == 0:
        turtle.fd(size)
        
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
def main():
    turtle.setup(800,400)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-700,-300)
    turtle.pendown()
    turtle.pensize(2)
    koch(1200,4)
    turtle.hideturtle()
    turtle.done()
main()