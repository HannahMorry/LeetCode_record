'''
Author: Hannah
Date: 2024-08-07 01:36:37
LastEditTime: 2024-08-07 01:36:56
'''
#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangle_sum = []
        for n in range(len(triangle)):

            if n == 0:
                triangle_sum.append(triangle[0])
            elif n == 1:
                triangle_sum.append([value + triangle[0][0] for value in triangle[1]])
            else:
                first_value = [triangle[n][0] + triangle_sum[n-1][0]]
                mid_value = [triangle[n][i] + min(triangle_sum[n-1][i-1], triangle_sum[n-1][i]) for i in range(1, n)]
                last_value = [triangle[n][-1] + triangle_sum[n-1][-1]]
                triangle_sum.append(first_value + mid_value + last_value)
        
        return min(triangle_sum[-1])
# @lc code=end

