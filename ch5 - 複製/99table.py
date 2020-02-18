# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:15:24 2016

@author: user
"""
for i in range(1, 10):  #外圈
    for j in range(1, 10):  #內圈
        print('%d*%d=%2d  '%(i,j,i*j), end='')
    print('\n')
