# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 15:14:42 2016

@author: user
"""
import random as rd
for i in range(1, 10):  #外圈
    for j in range(1, 10):  #內圈
        num=rd.randint(0,9)  
        print('%3d'%(num), end='')
    print('\n')