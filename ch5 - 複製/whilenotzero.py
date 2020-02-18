# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:07:56 2016

@author: user
"""
import random as rd
num=rd.randint(0,9) 
count=1
while num!=0:
    print(num)
    num=rd.randint(0,9) 
    count+=1
print(num)
print('%s%d%s' %('共產生亂數',count,'次'))   
    
