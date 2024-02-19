# -*- coding: utf-8-*-
"""
Created on Thu Jul 13 22:18:38 2017

@author: Richard祥
"""

def data_read(filename) :
    result = []
    with open(filename,'r') as f :
        for line in f:
            lines = list((line.replace(',',' ').replace('\n','').replace('{','').replace('}','').split(' ')))
            for i in range(len(lines)) :
                result.append(lines[i])
        print(result)
