from multiprocessing import Pool
from random import random
from math import sqrt
import time 
def mtkl(Drats) :
    hits = 0
    for i in range(0,Drats):
        x,y = random(),random()
        dis = sqrt(x**2+y**2)
        if dis <= 1.0 :
            hits = hits+1
    return hits
if __name__ == '__main__':
    pool = Pool(12)
    time1 = time.perf_counter()
    testlist = [2**27,2**27,2**27,2**27,2**27,2**27,2**27,2**27]
    hlist = pool.map(mtkl,testlist)       
    pi = 4*(sum(hlist)/2**30)
    Pool.close()    
    Pool.join()
    time2 = time.perf_counter()
    print('Sub-process(es) done')
    print('Pi is ',pi)
    print('Time is',time2-time1)
    #多进程快的不是提个档次！！！