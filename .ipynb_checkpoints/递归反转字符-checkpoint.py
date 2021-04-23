# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:55:57 2017

@author: Richard祥
"""

def reverse(s): 
    if s == s[::-1]:#负号代表倒序，以间隔为1分隔
        return s
    else:
        return reverse(s[1:])+s[0]
def main():
    s=input('Enter a string:')
    v=reverse(s)
    print(v)
main()