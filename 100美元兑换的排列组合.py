# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 17:10:57 2017

@author: Richard祥
"""

def make_change(amount,coins,hand=[]):
    if amount == 0:
        yield hand
    else :
        for coin in coins :
            if coin > amount or (len(hand) > 0 and hand[-1] < coin):
                continue
            else :
                for result in make_change(amount-coin,coins=coins,hand=hand+[coin]):
                    yield result
for way in make_change(100,coins=[10,25,50]):
    print(way)