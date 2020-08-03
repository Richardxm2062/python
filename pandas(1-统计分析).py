# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 21:16:10 2017

@author: Richard祥
"""

import numpy as np 
import pandas as pd
np.random.seed(1)
arr = np.random.rand(4)
d1 = pd.Series(2*np.random.normal(size=100)+3)
d2 = np.random.f(2,4,size=100)
d3 = np.random.randint(1,100,size=100)
df = pd.DataFrame(np.array([d1,d2,d3]).T,columns=['X1','X2','X2'])