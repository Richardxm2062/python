# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 08:21:36 2017

@author: Richard祥
"""

import numpy as np
from random import randint
i = 4
s = [[3,3],[2,2],[3,2],[3,0]]
t = [[0,0],[1,1],[0,1],[0,3]]
A = [[0,0],[0,1],[0,2],[0,3],[1,1],[2,2],[3,3],[3,2],[3,1],[3,0]]   #允许集合状态
D = [[1,1],[1,0],[0,1],[2,0],[0,2]]   #允许决策状态


def carry (s,t,i,way):
    global A
    if (-1)**i == -1 :
        p1 = np.array(s)[i-1] - np.array(way) 
        p2 = np.array(t)[i-1] + np.array(way)
        p1 = p1.tolist()
        p2 = p2.tolist()
        if p1 in A :
            s.append(p1)
            t.append(p2)
            i += 1
            return (s,t,i)
        else :
            return (s,t,i)
            pass
        
    if (-1)**i == 1 :
        p1 = np.array(s)[i-1] + np.array(way) 
        p2 = np.array(t)[i-1] - np.array(way) 
        p1 = p1.tolist()
        p2 = p2.tolist()
        if p1 in A  :
            s.append(p1)
            t.append(p2)
            i += 1
            return (s,t,i)
        else : 
            return (s,t,i)
            pass 


def loop(s,t,i) :
    global D
    for num in range(8): 
        if [0,0] not in s:
            random = randint(0,4)
            way = D[random]
            (s,t,i) = carry(s,t,i,way)
            if [0,0] not in s :
                continue
            else:
                return (s,t,i)
        else :
            return (s,t,i)
    return (s,t,i)
for k in range(2**50) :
    (s,t,i) = loop(s,t,i)
    if [0,0] not in s :
        i = 4
        s = [[3,3],[2,2],[3,2],[3,0]]
        t = [[0,0],[1,1],[0,1],[0,3]]
        print('第',k+1,'次暴力求解失败，进行下一次暴力求解。')
        continue
    else :
        print('通过暴力求解的s路径为',s)
        print('通过暴力求解的t路径为',t)
        print('最后求解次数为',k+1)
        break