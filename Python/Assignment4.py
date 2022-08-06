# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 08:54:16 2022

@author: Admin
"""

#Assignment Question 4
def questionFive(num_list):
firstElement = num_list[0] 
lastElement = num_list[-1]
if (firstElement == lastElement):
return True
else:
return False

xlistx = [10, 20, 30, 40, 190]

print (questionFive(xlistx))