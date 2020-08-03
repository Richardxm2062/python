# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:18:59 2017

@author: Richard祥
"""
def addInterest(balance,rate):
    newbalance = balance*(1+rate)
    return newbalance
def main():
    amount = 1000
    rate = 0.05
    amount = addInterest(amount,rate) 
    print(amount)    
main()