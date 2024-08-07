'''
Author: Hannah
Date: 2024-08-01 00:06:14
LastEditTime: 2024-08-01 15:14:27
'''
#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_length = 0
        for i in range(0, len(s)):
            continuous_letters = set()
            current_substring_length = 0
            if len(s) - i < longest_substring_length:
                break
            else:
                for j in range(i, len(s)):
                    string_letter = s[j]
                    if string_letter in continuous_letters:
                        break
                    else:
                        continuous_letters.add(string_letter)
                        current_substring_length += 1
            if current_substring_length > longest_substring_length:
                longest_substring_length = current_substring_length
        
        return longest_substring_length
        
        
# @lc code=end

