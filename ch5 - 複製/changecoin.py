# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:30:43 2015

@author: user
"""
count = 0
for x in range(6):
    for y in range(11):
        for z in range(51):
            if 10*x+5*y+z == 50:
                count = count + 1
print('%s %d %s' %('共有', count, '種換法'))
