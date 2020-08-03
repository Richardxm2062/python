# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:54:35 2017

@author: Richard祥
"""

def createTable(principal,apr):
    for year in range(1,11):
        principal = principal*(1+apr)
        print('%2d'%year,end='')
        # %2d 中2d的内容被后文%后的year替换同时为两个字符。
        #end=''保证print后不换行以确保下一个print紧跟
        total = caculateNum(principal)
        print('*' * total)#字符串“ * ”乘以它应该有的数量“Total”
    print('  2K    6K    10K    14K    18K')
    #间距以一个“ * ”代表一千也代表一个字符
def caculateNum(principal):
    total = int(principal*6/1000.0)
    return total
def main():
    print('This program plots the growth of a 10-year investment.')
    principal = eval(input('Enter the initial principal:'))
    apr = eval(input('Enter the anniualized interest rate:'))
    createTable(principal,apr)
main()        
        