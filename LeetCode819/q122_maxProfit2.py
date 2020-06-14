from typing import List

def maxProfit(self, prices:List[int]) -> int:
    if len(prices) < 2:
        return 0
    total = 0
    for i in range(1, len(prices)):
        profit = prices[i] - prices[i-1]
        if profit >= 0:
            total += profit
    return total

prices = [7,1,5,3,6,4]    
res = maxProfit(123, prices)
print(res)