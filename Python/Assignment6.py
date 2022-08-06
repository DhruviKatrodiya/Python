# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 18:44:20 2022

@author: HP
"""

sampleList = [34, 54, 67, 89, 11, 43, 94]
print(); print("Origigal list ", sampleList)

element = sampleList.pop(4)
print(); print("List After removing element at index 4 ", sampleList)

sampleList.insert(2, element)
print(); print("List after Adding element at index 2 ", sampleList)

sampleList.append(element)
print(); print("List after Adding element at last ", sampleList)
