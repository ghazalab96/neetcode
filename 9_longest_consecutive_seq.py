from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:  # check for an empty list
            return 0
        set_of_nums = set(nums)
        longest_streak = 0
        for num in set_of_nums:
            if (num - 1) not in set_of_nums:
                current_num = num
                current_streak = 1

                while (current_num + 1) in set_of_nums:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)

                
        return longest_streak

solution = Solution()
answer = solution.longestConsecutive([2,20,4,10,3,4,5])
print(answer)