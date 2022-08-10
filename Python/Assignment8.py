# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 09:13:04 2022

@author: Admin
"""


import collections

a_list = ["a", "b", "a", "a"]
occurrences = collections.Counter(a_list)
print(occurrences)

o/p:-
    Counter({'a': 3, 'b': 1})
