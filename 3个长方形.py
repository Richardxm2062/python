# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:01:37 2017

@author: Richard祥
"""

import turtle 

def Threegechangfangxing(x) :
    for i in range(3):
        if x >= 150  :
            turtle.penup()
            turtle.goto(-x,-0.618*x)
            turtle.pendown()
            turtle.fd(2*x)
            
            turtle.circle(0.001,90)
            turtle.fd(2*0.618*x)
            
            turtle.circle(0.001,90)
            turtle.fd(2*x)
            
            turtle.circle(0.001,90)
            turtle.fd(2*0.618*x)
            turtle.circle(0.001,90)
            x = x - 50
        else :
            break
def main():
    turtle.setup(1300,800,0,0)
    turtle.pencolor('blue')
    turtle.pensize(5)
    Threegechangfangxing(300)
main()         