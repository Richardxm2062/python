
import numpy as np
import math 

def time(x):
    x = np.array(x)
    sumtime = np.sum(x)
    allhtime = sumtime / (60*1.5)
    dhtime = math.modf(allhtime)
    lefttime = dhtime[0] * 60
    print("需要",dhtime[1],"小时",lefttime,"分钟")    
    

def main():
    x = input("Please input the x \n")
    x = [int(n) for n in x.split()]
    time(x)


main()

