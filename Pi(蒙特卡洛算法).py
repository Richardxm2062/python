from random import random
from math import sqrt
from time import clock
def mtkl(DRATS) :
    hits = 0
    for i in range(0,DRATS):
        x,y = random(),random()
        dis = sqrt(x**2+y**2)
        if dis <= 1.0 :
            hits = hits+1
    pi = 4*(hits/DRATS)
    return pi 
time1 = clock()
pi = mtkl(2**20)
print(pi)     
time2 = clock()
print(time2-time1) 
'''tl = [2**25,2**25,2**25]
time1 = clock()
for i in tl :
    pi = mtkl(i)
    print(pi)
time2 = clock()
print(time2-time1)'''