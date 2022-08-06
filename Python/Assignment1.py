# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 08:16:59 2022

@author: Admin
"""

#Assignment Question 1
def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if num1*num2 <= 1000:
        return num1*num2
    else:
        return num1+num2 

result = multiplication_or_sum(20,30)
print("The result is = ", result)

result = multiplication_or_sum(50,10)
print("The result is = ", result)


