
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = dict()
        res = 0
        l = 0
        for r in range(len(s)):
            characters[s[r]] = 1 + characters.get(s[r], 0)
           
            while (r - l + 1) - max(characters.values()) > k:
                characters[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

