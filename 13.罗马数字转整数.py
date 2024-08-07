'''
Author: Hannah
Date: 2024-08-04 00:31:42
LastEditTime: 2024-08-04 00:45:28
'''
#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = {'I':1 , 'V':5 ,'X':10 ,'L':50 ,'C':100 ,'D':500 ,'M':1000}
        Int = 0
        n = len(s)
        for i in range(n-1):
            if Roman[s[i]] < Roman[s[i+1]]:
                Int -= Roman[s[i]]
            else:
                Int += Roman[s[i]]
        return Int + Roman[s[-1]]
# @lc code=end

