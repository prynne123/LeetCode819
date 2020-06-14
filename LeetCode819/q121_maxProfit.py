from typing import List

def maxProfit(self, prices:List[int]) -> int:
    if not prices:
        return 0
    cur_min = prices[0]
    profit = 0
    for i in range(len(prices)):
        cur_min = min(cur_min, prices[i])
        profit = max(profit, prices[i]-cur_min)
    return profit
    
prices = [7,1,5,3,6,4]
res = maxProfit(123,prices)
print(res)