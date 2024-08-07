'''
Author: Hannah
Date: 2024-08-02 22:42:53
LastEditTime: 2024-08-02 22:59:05
'''
#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ''
        for i in range(len(s)):
            if len(longest_palindrome) > len(s)-i:
                return longest_palindrome
            else:
                for j in range(i, len(s)):
                    substring = s[i:j+1]
                    palindrome = substring[::-1]
                    if substring == palindrome and len(substring) > len(longest_palindrome):
                        longest_palindrome = substring
        return longest_palindrome
# @lc code=end

