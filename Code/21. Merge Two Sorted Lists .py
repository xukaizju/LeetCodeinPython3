# -*- coding: utf-8 -*-
"""
Created on Sat Dec 9 15:43:17 2017

@author: Einstein
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        ret = ListNode(0)
        head = ret
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                ret.next = l2
                l2 = l2.next
            else:
                ret.next = l1
                l1 = l1.next
            ret = ret.next

        if l1 == None:
            ret.next = l2

        if l2 == None:
            ret.next = l1
        return head.next

#test
# a = ListNode(1)
# n = a
# n.next = ListNode(5)
# n = n.next
# n.next = ListNode(7)
# n = n.next
#
# b = ListNode(1)
# m = b
# m.next = ListNode(2)
# m = m.next
# m.next = ListNode(3)
# m = m.next
#
# s = Solution()
# q = s.mergeTwoLists(a, b)
# print (q.val)
# print (q.next.val)
# print (q.next.next.val)
# print (q.next.next.next.val)
# print (q.next.next.next.next.val)
# print (q.next.next.next.next.next.val)
