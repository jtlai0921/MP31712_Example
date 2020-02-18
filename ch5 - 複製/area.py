# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:49:10 2016

@author: user
"""
#放大縮小
#dx=1
#area=0
#y=0
#for x in range(200,500,dx):
#    x=x/100
#    y=(x**2)+1
#    area=area+(y*(dx/100))
#print('area = ', area)   
 
#使用numpy的arange 
import numpy as np
dx=float(input('Please input dx = '))
area=0
y=0
for x in np.arange(2,5,dx):
    y=(x**2)+1
    area=area+(y*dx)
print('area = ', area)    
    