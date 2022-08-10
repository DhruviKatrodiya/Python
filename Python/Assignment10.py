# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 09:16:55 2022

@author: Admin
"""



row=int(input("enter the number"))
for i in range(row):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\r")
          
        
O/p:-
    
enter the number 5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
