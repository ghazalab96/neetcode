class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_words, t_words = {}, {}

        for i in range(len(s)):
            s_words[s[i]] = 1 + s_words.get(s[i], 0)
            t_words[t[i]] = 1 + t_words.get(t[i], 0)
        return s_words == t_words