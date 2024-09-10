
from typing import List
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def remove_alphanumerical(s):
            return re.sub(r'[^\w\s]', '', s)
        
        return remove_alphanumerical(s).replace(" ", "").lower()[::-1] == remove_alphanumerical(s).replace(" ", "").lower()


solution = Solution()
print(solution.isPalindrome("tab a cat"))