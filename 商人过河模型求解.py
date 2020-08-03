# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 18:49:11 2017

@author: Richard祥
"""
import numpy as np

def sum(s,t,i,x):
    s = np.array(s)
    t = np.array(t)
    if (-1)**i == 1:
         s = s + x
         t = t - x 
    else:
        s = s - x
        t = t + x
    s = s.tolist()
    t = t.tolist()
    return (s,t)
    
def loop(i,n,s,t,D):
    sFinal = [0,0]
    tFinal = [3,3]
    A = [[0,0],[0,1],[0,2],[0,3],[1,1],[2,2],[3,3],[3,2],[3,1],[3,0]]
    D = [[1,1],[1,0],[0,1],[2,0],[0,2]]
    L = [[1,1],[1,0],[0,1],[2,0],[0,2]]
    if n in D:
        D.remove(n)
    else :
        pass
    if D :       
        for c in D :
            (ss,tt) = sum(s,t,i,c)
            if ss in A and tt in A :
                 K = tt == tFinal
                 V = ss == sFinal
                 if V and K :
                    print(c,2)
                    break
                 else :
                     print(c,3)
                     i += 1
                     D.remove(c)
                     loop2(i,c,s,t,D)
    else:
        print('失败，进行下一个值')  

def loop2(i,n,s,t,D):
    sFinal = [0,0]
    tFinal = [3,3]
    A = [[0,0],[0,1],[0,2],[0,3],[1,1],[2,2],[3,3],[3,2],[3,1],[3,0]]
    L = [[1,1],[1,0],[0,1],[2,0],[0,2]]
    if n in D:
        D.remove(n)
    else :
        pass
    if D :       
        for c in D :
            (ss,tt) = sum(s,t,i,c)
            if ss in A and tt in A :
                 K = tt == tFinal
                 V = ss == sFinal
                 if V and K :
                    print(c,2)
                    break
                 else :
                     print(c,3)
                     i += 1
                     D.remove(c)
                     loop2(i,c,s,t,D)
    else:
        print('深度循环失败，进行下一个值')  


i = 1
s = [3,3]  #初始此岸状态
t = [0,0]   #初始彼岸状态
sFinal = [0,0]   #目标此岸状态
tFinal = [3,3]   #目标彼岸状态
A = [[0,0],[0,1],[0,2],[0,3],[1,1],[2,2],[3,3],[3,2],[3,1],[3,0]]
D = [[1,1],[1,0],[0,1],[2,0],[0,2]]
L = [[1,1],[1,0],[0,1],[2,0],[0,2]]
K = t == tFinal
V = s == sFinal
while V == False or K == False :
    for nn in L:
        print(nn,0)
        (s,t) = sum(s,t,i,nn)
        if s in A and t in A :
            print(nn,1)
            loop(2,nn,s,t,D)
            i = 1
            s = [3,3]  #初始此岸状态
            t = [0,0]   #初始彼岸状态
            D = [[1,1],[1,0],[0,1],[2,0],[0,2]]
print('End')        