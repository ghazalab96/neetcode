from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in anagrams:
                anagrams[key] = [word]
            else:
                anagrams[key].append(word)
        return list(anagrams.values())