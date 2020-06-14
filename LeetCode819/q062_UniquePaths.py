# -*- coding: utf-8 -*-
# import math
from typing import List


class solution:
    def path2(self, m: int, n: int) -> int:
        if(m<1):
            return 0
        if(n<1):
            return 0
        #state
        dp = [[0]*n for i in range(m)]
        print(dp)
        #init
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        #function dp[m][n] = dp[m-1][n]+dp[m][n-1]
        for i in range(1,m):
            for j in range (1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        #result
        return dp[m-1][n-1]

m = 7
n = 3
sha = solution.path(111,m,n)
print('%d种'%sha)