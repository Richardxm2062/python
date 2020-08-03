# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:37:28 2017

@author: Richard祥
"""

import requests
from bs4 import BeautifulSoup
import re

rq = requests.get('https://book.douban.com/subject/1084336/comments/')
soup = BeautifulSoup(rq.text,'lxml')
pattern1 = soup.find_all('p','comment-content')
pattern2 = re.compile('a title="(.*?)" href="https://www.douban.com/people(.*?)"')
pattern2 = re.findall(pattern2,rq.text)
i = 1
for item1 in pattern1 :
    print('第',i,'条评论')
    print(item1.string)
    print('评论来自：',pattern2[i-1][0],'主页','https://www.douban.com/people%s'%pattern2[i-1][1])
    print('\n')
    i += 1 