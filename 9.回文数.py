'''
Author: Hannah
Date: 2024-08-03 19:15:12
LastEditTime: 2024-08-03 19:15:20
'''
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

# @lc code=end

