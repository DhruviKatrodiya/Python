# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 18:42:58 2022

@author: HP
"""

lower = 1
upper = 20

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)