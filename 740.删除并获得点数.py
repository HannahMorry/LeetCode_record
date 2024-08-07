'''
Author: Hannah
Date: 2024-08-04 23:37:47
LastEditTime: 2024-08-04 23:38:10
'''
#
# @lc app=leetcode.cn id=740 lang=python3
#
# [740] 删除并获得点数
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 统计每个数字出现的次数
        count = Counter(nums)
        # 找到数组中的最大值
        max_num = max(nums)
        
        # 使用 lru_cache 来缓存 dp 结果
        @lru_cache(None)
        def dp(x):
            if x == 0:
                return 0
            if x == 1:
                return count[1] * 1
            # 动态转移方程
            return max(dp(x - 1), dp(x - 2) + x * count[x])
        
        return dp(max_num)
# @lc code=end

