#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x_reversed = int(str(x)[::-1])
            if x_reversed > 2**31 - 1:
                return 0
            else:
                return x_reversed
        else:
            x_reversed = int('-'+str(abs(x))[::-1])
            if x_reversed < -2**31:
                return 0
            else:
                return x_reversed
# @lc code=end

