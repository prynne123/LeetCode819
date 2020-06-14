from typing import List

class solution:

    def twoSum2(self, nums: List[int], target: int):# -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            else:
                dict[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
#self参数传什么数据类型的都可以，传字符串要加单引号
res = solution.twoSum2(123, nums, target)
print(res)