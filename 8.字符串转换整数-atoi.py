'''
Author: Hannah
Date: 2024-08-03 17:21:16
LastEditTime: 2024-08-03 19:08:09
'''
#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def bound_value(self, value):
        if value > 2**31 -1 :
            return 2**31 - 1
        elif value < -2**31:
            return -2**31
        else:
            return value

    def myAtoi(self, s: str) -> int:

        num_list = list('0123456789')

        if len(s) == 0:
            return 0
        
        else:
            for i in range(len(s)):
                if s[i] != ' ':
                    start_idx = i
                    break
                if i+1 == len(s):
                    return 0

            if s[start_idx] not in (['+', '-'] + num_list):
                return 0

            elif s[start_idx] in ['+', '-']:
                if len(s[start_idx+1:]) == 0:
                    return 0
                else:
                    signal = s[start_idx]
                    for j in range(start_idx+1, len(s)):
                        if s[j] not in num_list:
                            if j == start_idx + 1:
                                return 0
                            else:
                                res = int(signal + s[start_idx+1:j])
                                return self.bound_value(res)
                    res = int(signal + s[start_idx+1:])
                    return self.bound_value(res)
                    
            else:
                if len(s[start_idx+1:]) == 0:
                    return int(s[start_idx])
                else:
                    for j in range(start_idx+1, len(s)):
                        if s[j] not in num_list:
                            if j == start_idx + 1:
                                return int(s[start_idx])
                            else:
                                return self.bound_value(int(s[start_idx:j]))
                    return self.bound_value(int(s[start_idx:]))




# @lc code=end

