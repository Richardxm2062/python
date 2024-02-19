from random import random
from math import sqrt
import time
def mtkl(DRATS) :
    hits = 0
    for i in range(0,DRATS):
        x,y = random(),random()
        dis = sqrt(x**2+y**2)
        if dis <= 1.0 :
            hits = hits+1
    pi = 4*(hits/DRATS)
    return pi 
time1 = time.perf_counter()
pi = mtkl(2**28)
print(pi)     
time2 = time.perf_counter()
print(time2-time1) 
