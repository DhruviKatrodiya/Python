# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 09:13:04 2022

@author: Admin
"""


row=int(input("enter the number"))
for i in range(row):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\r")