from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_of_nums = {}
        for num in nums:
            set_of_nums[num] = 1 + set_of_nums.get(num,0)
        
        sorted_nums = sorted(set_of_nums.items(), key=lambda item: item[1], reverse=True)
        
        return [item[0] for item in sorted_nums[:k]]