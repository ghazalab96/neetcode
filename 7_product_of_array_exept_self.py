from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = list()
        for num in nums:
            new_nums = nums[:]
            new_nums.remove(num)
            c = 1
            for new_num in new_nums:
                c = new_num * c
            output.append(c)
        return output