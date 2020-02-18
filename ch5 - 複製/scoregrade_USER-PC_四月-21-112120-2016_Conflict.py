# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:23:52 2016

@author: user
"""
score=int(input('請輸入成績0-100分: '))
if score<60:   #條件1
    print('戊等')
elif score <70:  #條件2
    print('丁等')
elif score<80: #條件3
    print('丙等')    
elif score<90: #條件4
    print('乙等')
elif score<100: #條件5
    print('甲等')
else:  #條件6
    print('輸入錯誤')        
