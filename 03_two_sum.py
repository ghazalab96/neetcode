from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_of_nums = {}
        for i, n in enumerate(nums):
            new_target = target - n
            if new_target in set_of_nums:
                return [set_of_nums[new_target], i]
            set_of_nums[n] = i