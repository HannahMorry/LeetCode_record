'''
Author: Hannah
Date: 2024-07-31 11:41:33
LastEditTime: 2024-07-31 22:46:37
'''
#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
# @return a ListNode
    def addTwoNumbers(self, l1, l2):
        def lnode_to_int(lnode):
            num_str = ''
            while lnode:
                num_str += str(lnode.val)
                lnode = lnode.next
            return int(num_str[::-1])
        
        num1 = lnode_to_int(l1)
        num2 = lnode_to_int(l2)
        num_sum = str(num1 + num2)[::-1]

        dummy = current = ListNode(0)

        for num in num_sum:
            current.next = ListNode(int(num))
            current = current.next
        
        return dummy.next

# @lc code=end

