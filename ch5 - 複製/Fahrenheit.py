# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 15:11:50 2016

@author: user
"""
data=input('請輸入華氏溫度： ')
if data.isdigit():
    Fahrenheit=int(data)
    Celsius=(5/9)*(Fahrenheit-32)
    print('攝氏溫度為', round(Celsius,1))
else:
    print('請輸入數值資料')
        
