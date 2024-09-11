from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            second_number = target - numbers[i]
            if second_number in numbers:
            
                return [i + 1, numbers.index(second_number) + 1]
                
solution = Solution()
answer = solution.twoSum(numbers = [1,2,3,4], target = 7)
print(answer)