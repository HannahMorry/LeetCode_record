'''
Author: Hannah
Date: 2024-08-07 00:56:40
LastEditTime: 2024-08-07 00:57:02
'''
#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If the starting point or the ending point is an obstacle, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # Initialize the first cell
        obstacleGrid[0][0] = 1
        
        # Initialize the first column
        for i in range(1, m):
            obstacleGrid[i][0] = obstacleGrid[i-1][0] if obstacleGrid[i][0] == 0 else 0
        
        # Initialize the first row
        for j in range(1, n):
            obstacleGrid[0][j] = obstacleGrid[0][j-1] if obstacleGrid[0][j] == 0 else 0
        
        # Fill the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        
        return obstacleGrid[m-1][n-1]
# @lc code=end

