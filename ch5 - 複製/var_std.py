# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:25:54 2016

@author: user
"""
import math
sample=[5,8,9,6,4,1,5,3,6,2]
n=len(sample)
mean=sum(sample)/n
sumi=0
for i in range(0, n):
    sumi=sumi+((sample[i]-mean)**2)
var=sumi/(n-1)    
std=math.sqrt(var)
print('sample = ', sample)
print('mean = ', mean)
print('max = ', max(sample))
print('min = ', min(sample))
print('variance = ', round(var,2))
print('standard deviation = ', round(std,2))

