# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 08:52:32 2017

@author: Einstein
"""
def twoSum(nums, target):
    n=len(nums)
    a=0
    b=1
    while a<n:
        while b<n:
            if nums[a]+nums[b]==target:
                return [a,b]
            else:
                b+=1
        a+=1
        b=a+1
