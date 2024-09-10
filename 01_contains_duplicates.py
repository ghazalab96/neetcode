from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_of_nums = set()
        for num in nums:
            if num in set_of_nums:
                return True
            set_of_nums.add(num)
        return False