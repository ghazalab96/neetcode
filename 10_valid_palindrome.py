from typing import List
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def remove_alphanumerical(s):
            return re.sub(r'[^\w\s]', '', s)
        
        s_new = remove_alphanumerical(s).replace(" ", "").lower()
        n = len(s_new)
        for i in range(n//2):
            if s_new[i] != s_new[n-1-i]:
                return False
        return True



solution = Solution()
print(solution.isPalindrome("tab a cat"))