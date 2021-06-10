# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 21:46:54 2017

@author: Richard祥
"""

def data_time_read(filename) :
    result_time=[]
    with open(filename,'r') as file :
        for line in file :
            lines=list(line.replace(',',' ').replace('\n','').replace('{','').replace('}','').split(' '))
            lines=lines[1::2]
            for i in range(len(lines)):
                result_time.append(lines[i])
    return result_time
def data_angle_read(filename) :
    result_angle=[]
    with open(filename,'r') as file :
        for line in file :
            lines=list(line.replace(',',' ').replace('\n','').replace('{','').replace('}','').split(' '))
            lines=lines[1::2]
            for i in range(len(lines)):
                result_angle.append(lines[i])
    return result_angle
def main() :
    f1=input('Please type the name of the first file about time :')
    f2=input('Please type the name of the second file about angle :')
    result_time_final=data_time_read(f1)
    result_angle_final=data_angle_read(f2)    
    with open('New_time_data.txt','w') as file :
        for i in range(len(result_time_final)):
            file.write(result_time_final[i])
            file.write('\n')
    with open('New_angle_data.txt','w') as file :
        for i in range(len(result_angle_final)):
            file.write(result_angle_final[i])
            file.write('\n')
main()
        