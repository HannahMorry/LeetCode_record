'''
Author: Hannah
Date: 2024-08-02 23:08:34
LastEditTime: 2024-08-03 15:44:01
'''
#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        result = ['' for _ in range(numRows)]

        for i in range(numRows):
            if i == 0 or i == numRows-1:
                result[i] = s[i::2*numRows-2]
            else:
                a = [j for j in range(i, len(s), 2*numRows-2)]
                result[i] = ''.join(
                    [s[j] + (s[j+2*(numRows-i-1)] if (j+2*(numRows-i-1)) < len(s) else '') 
                     for j in range(i, len(s), 2*numRows-2)]
                )

        return ''.join(result)
# @lc code=end

