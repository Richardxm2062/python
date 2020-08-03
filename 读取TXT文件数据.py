# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 20:39:58 2017

@author: Richard祥
"""

def read_data(filename):
    lin = []
    with open(filename,'r',encoding='utf-8') as f :
        for line in f:
            lines = list(line.replace('\n','').split(' '))
            print(lines)
            if lines :
                for i in range(len(lines)): 
                    lin.append(lines[i])
            else :
                continue
    return lin
def main():
    file=input('Write the filename: ')
    result=read_data(file)
    with open('Data.txt','w') as files:
        if result :
            for i in range(len(result)) :
                    files.write(result[i])
                    files.write('\n')
        else :    
            pass
main()