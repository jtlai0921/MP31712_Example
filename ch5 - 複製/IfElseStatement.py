# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math 
num=int(input('請輸入數據1-100: '))
if num<50:
    total=math.sqrt(num)*10
    print('total=%d' % round(total))
else: 
    total=num+10
    print('total=%d' % round(total))