# -*- coding: utf-8 -*-
"""
Created on Mon May 29 21:37:35 2017

@author: Richard祥
"""
def fibonacci(n):
    terms = [0,1]
    i = 2
    while i<=n:
        terms.append(terms[i-1]+terms[i-2])
        i= i + 1
    return terms[n]
def main():
    n = int(input('Enter a number in fibonacci:'))
    print(fibonacci(n))
main()