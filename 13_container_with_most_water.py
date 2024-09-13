from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_output = 0
        for index_1, value_1 in enumerate(heights):
            heights_2 = heights.copy()
            heights_2.pop(index_1)
            for index_2, value_2 in enumerate(heights_2):
                output = abs(index_1 - index_2) * min(value_1, value_2)
                if output > max_output:
                    max_output = output

        return max_output