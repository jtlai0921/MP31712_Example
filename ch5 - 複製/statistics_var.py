# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:19:56 2016

@author: user
"""

import statistics as st
sample=[5,8,9,6,4,1,5,3,6,2]
print('sample = ', sample)
print('mean = ',  st.mean(sample))
print('mean = ',  max(sample))
print('mean = ',  min(sample))
print('variance = ', round(st.variance(sample),2))
print('standard deviation = ',  round(st.stdev(sample),2))


