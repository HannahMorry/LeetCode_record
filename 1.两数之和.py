'''
Author: Hannah
Date: 2024-07-20 21:23:19
LastEditTime: 2024-07-31 11:28:03
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            hashmap[num] = i
        return []
# @lc code=end

