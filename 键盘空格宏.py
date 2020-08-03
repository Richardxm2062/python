# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:13:22 2017

@author: Richard祥
"""

import win32api
import win32con
import time
i = 0
while i<1:    
    time.sleep(0.5)
    win32api.keybd_event(32,0,0,0) #空格键位码是32
    win32api.keybd_event(32,0,win32con.KEYEVENTF_KEYUP,0) #释放按键                                  