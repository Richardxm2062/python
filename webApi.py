# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 15:50:16 2017

@author: Richard祥
"""
import requests
rq = requests.get('https://api.douban.com//v2/movie/subject/1291546')
data = rq.json()
print('电影名字为:',data['title'],'\n''平均得分为:',data['rating']['average'])