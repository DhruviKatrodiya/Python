# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 08:47:22 2022

@author: Admin
"""


#Assignment Question 2
num = list(range(10))
previousNum = 0
for i in num:
    sum = previousNum + i
    print('Current Number '+ str(i) + 'Previous Number ' + str(previousNum) + 'is ' + str(sum)) # <- This is the issue.
    previousNum=i
