# -*- coding: utf-8 -*-
"""
Created on S Dec 10 10:24:15 2017

@author: Einstein
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.generateParenthesisIter('',n, n)
        return self.res
    def generateParenthesisIter(self, mstr, r, l):
        if r==0 and l==0:
            self.res.append(mstr)
        if l>0:
            self.generateParenthesisIter(mstr+'(',r,l-1)
        if r>0 and r>l:
            self.generateParenthesisIter(mstr+')',r-1,l)
s = Solution()
a = s.generateParenthesis(3)
print (a)
