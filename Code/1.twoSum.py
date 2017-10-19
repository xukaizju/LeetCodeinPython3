# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 08:52:32 2017

@author: Einstein
"""
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for i in range(len(num)):
            x = num[i]
            if target-x in dict:
                return (dict[target-x], i)
            dict[x] = i
