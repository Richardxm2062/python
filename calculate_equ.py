# -*- coding: utf-8 -*-
# @time: 2018-4-4
# @author: Zhang Yuning
# @institute: Chongqing University

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pylab as plt

# four vars for each iteration
# Ts->C1->Tx->C2->Ts

def cal_Tx(C,t):
    return C*np.exp(-17.22*t)+333.15

def cal_Ts(C,t):
    return C*np.exp(-22.02*t)+249.15

def cal_C1(T,t):
    return (T-333.15)/np.exp(-17.22*t)

def cal_C2(T,t):
    return (T-249.15)/np.exp(-22.02*t)

def obj_func(t,a,b,k):
    return a*(1-np.exp(-k*t))+b

# parameters for simulation
iter_N=300000
delta_t=10**(-6)


# array to store the data 
T_arr=np.zeros(iter_N+1)

# initial_state
Ts=249.15
T_arr[0]=Ts
Tx=0
n=0

while n<iter_N:
    C1=cal_C1(Ts,n*delta_t)
    n+=1
    Tx=cal_Tx(C1,n*delta_t)
    T_arr[n]=Tx
    C2=cal_C2(Tx,n*delta_t)
    n+=1
    Ts=cal_Ts(C2,n*delta_t)
    T_arr[n]=Ts

t=np.arange(iter_N+1)*delta_t

popt, pcov=curve_fit(obj_func,t,T_arr)
perr = np.sqrt(np.diag(pcov))

fig=plt.figure()
plt.plot(t,T_arr,label='simulation data')
plt.plot(t,obj_func(t,*popt),'r--',label='fitting curve')
plt.legend(loc='lower right')
plt.title('Gas temperature-Time')
plt.ylabel('T/K')
plt.xlabel('t/s')
fig.dpi=300
plt.grid(True)
plt.annotate('T=286.01−36.86∗e^(−19.62)t', xy=(0.1, 280), xytext=(0.15, 279.5),
            arrowprops=dict(facecolor='black', width=1,headwidth=5,shrink=0.05),
            )

plt.show()

print('------------------------')
print('Optimal parameters:\na:{0}\nb:{1}\nk:{2}'.format(*popt))
print('------------------------')
print('Error for parameters:\n{0}\n{1}\n{2}'.format(*perr))