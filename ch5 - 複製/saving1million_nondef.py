# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 10:15:40 2015

@author: user
"""
mpv=10000  #月存金額
ypv=120000  #年存金額
r=0.02  #年利率
target=1000000  #目標存款
#月複利
mfv=0  #月複利累計金額
n=0  #期數
while mfv<target:
    mfv=(mpv+mfv)*(1+r/12) 
    n=n+1
print('%s %.2f %s %.2f %s' %('月存1萬,約', n/12, '年可以存到', mfv, '元'))
#年複利
yfv=0 #年複利累計金額
n=0
while yfv<target:
    yfv=(ypv+yfv)*(1+r)
    n=n+1
print('%s %.2f %s %.2f %s' %('年存12萬,約', n, '年可以存到', yfv, '元'))