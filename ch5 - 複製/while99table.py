# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 20:51:23 2016

@author: user
"""
i=1
j=1
while i<=9: #外圈
    if i==4:
        i+=1
        continue
    while j<=9:  #內圈
        if j==7:
            break
        print('%d*%d=%2d  '%(i,j,i*j), end='')
        j+=1
    j=1
    i+=1
    print('\n')    





#for i in range(1, 10):  #外圈
#    for j in range(1, 10):  #內圈
#        print('%d*%d=%2d  '%(i,j,i*j), end='')
#    print('\n')
