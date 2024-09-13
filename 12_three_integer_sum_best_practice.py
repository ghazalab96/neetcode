from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, value in enumerate(nums):
            if value > 0:
                break

        
            if index > 0 and value == nums[index - 1]:
                continue
            l, r = index + 1, len(nums) - 1
            while l < r:
                three_sum = value + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([value, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
