class Solurion:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window and two pointers
        l = 0  # left pointer
        res = 0  # max len of sequence without duplicate
        seq = set()  # we meed a set to check the duplicates

        for r in range(len(s)):  # right pointer going through letters, one by one
            while s[r] in seq:
                seq.remove(s[l])    # pop the characters from the left side of seq until we get rid of the duplicates
                l += 1      # updating the position of left pointer
            seq.add(s[r])       # since the seq doesn't have s[r], now we add it to the seq
            res = max(res, r - l + 1)  # updating the result
        return res

