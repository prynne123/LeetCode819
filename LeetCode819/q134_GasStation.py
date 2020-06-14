from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    
        if sum(gas)<sum(cost):
            return -1
        curr_gas = 0
        start = 0
        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]
            if curr_gas<0:
                start = i+1
                curr_gas = 0
        return start
        
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
res = Solution.canCompleteCircuit(123, gas, cost)
print(res)