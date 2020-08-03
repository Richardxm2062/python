# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 23:27:22 2017

@author: Richard祥
"""
from turtle import Turtle
def main():
    p = Turtle()
    p.color('green')
    p.pensize(5)
    p.hideturtle()#隐藏箭头的样子
    p.getscreen().tracer(30,0)
    #Turtle.getscreen()意思为返回一个TurtleScreen类的绘图对象，并开启绘画
    #tracer()方法是动画控制的
    #第一个参数若被指定，只有每一个n次定期屏幕更新真的执行，（可以用来加速复杂图形的绘制）
    #第二个参数设置延迟值，设置或返回以毫秒为单位的绘图延迟
    p.left(90)
    p.penup()
    p.goto(0,-200)
    p.pendown()
    tree([p],200,65,0.6375)
    p.speed(1)
def tree(plist,l,a,f):
    if l > 5 :
        lst = []
        for p in plist:
            p.fd(l)
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst,l*f,a,f)
main()
        
            