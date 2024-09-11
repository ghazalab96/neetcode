from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        set_of_triplets = set()

        for index, value in enumerate(nums):
            nums_2 = nums.copy()
            nums_2.pop(index)
            for index_2, value_2 in enumerate(nums_2):
                nums_3 = nums_2.copy()
                nums_3.pop(index_2)
                for index_3 in range (len(nums_3)):
                    if nums[index] + nums_2[index_2] + nums_3[index_3] == 0:
                        x = (nums[index], nums_2[index_2], nums_3[index_3])
                        final_triplets = tuple(sorted(x))
                        set_of_triplets.add(final_triplets)


        final_list = [list(t) for t in set_of_triplets]
        return final_list

              

solution = Solution()
print(solution.threeSum(nums = [-1,0,1,2,-1,-4]))