# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 15:19:56 2017

@author: Richard祥
"""

import numpy as np 
import pandas as pd
arr1 = np.arange(1,6,2)
s1 = pd.Series(arr1)
dic1 = {'a':10,'b':20,'c':30,'d':50,'e':60}
arr2 = np.arange(12).reshape(4,3)
df1 = pd.DataFrame(arr2)
dic2 = {'a':[1,2,3,4],'b':[5,6,7,8],'c':[9,10,11,12],'d':[13,14,15,16]}
dic3 = {'one':{'a':1,'b':2,'c':3,'d':4},'two':{'a':9,'b':10,'c':11,'d':12},'three':{'a':5,'b':6,'c':7,'d':8}}
dic4 = pd.DataFrame(dic3)[['one','three']]
s4 = pd.Series(np.array([1,1,2,3,5,8]))
s4.index = ['a','b','c','d','e','f']
s5 = pd.Series(np.array([10,15,20,30,55,80]))
s5.index = ['a','b','c','d','e','f']
s6 = pd.Series(np.array([12,11,13,15,14,16]))
s6.index = ['a','b','c','d','e','f']
df2 = {'Name':['Alfred','Alice','Barbara','Carol','Henry'],'Sex':['M','F','F','F','M'],'Age':[14,13,13,14,14],'Height':[69.0,56.5,65.3,62.8,63.5],'Weight':[112.5,84.0,98.0,102.5,102.5]}
df3 = pd.DataFrame(df2)
names=df3['Name']
df3.drop(labels='Name',axis=1,inplace=True)
df3.insert(0,'Name',names)
sex = df3['Sex']
df3.drop(labels='Sex',axis=1,inplace=True)
df3.insert(1,'Sex',sex)