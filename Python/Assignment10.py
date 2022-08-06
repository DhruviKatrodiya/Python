# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 09:16:55 2022

@author: Admin
"""


row=int(input("Enter the number"))
for i in range (row):
    for j in range(i+1):
        print(j+1, end=" ")
        