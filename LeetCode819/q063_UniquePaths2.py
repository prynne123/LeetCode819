# -*- coding: utf-8 -*-
#import math
from typing import List
class solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if (m < 1):
            return 0
        if (n < 1):
            return 0
        #state
        dp = [[0]*n for i in range(m)]
        #init
        for i in range(m):
            if (obstacleGrid[i][0] == 1):
                break
            dp[i][0] = 1

        for j in range(n):
            if (obstacleGrid[0][j] == 1):
                break
            dp[0][j] = 1
        #function dp[m][n] = dp[m-1][n]+dp[m][n-1]
        for i in range(1,m):
            for j in range (1,n):
                if(obstacleGrid[i][j] == 1):
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        #result
        return dp[m-1][n-1]

m = 3
n = 3
obstacleGrid = [[0]*n for i in range(m)]
obstacleGrid[1][1] = 1
sha = solution.uniquePathsWithObstacles(111,obstacleGrid)
print('%d种'%sha)