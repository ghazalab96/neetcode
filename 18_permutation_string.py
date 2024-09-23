class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = l + len(s1) - 1
        set_1 = list()
        set_2 = list()
        for letter in s1:
            set_1.append(letter)
        while r <= len(s2) - 1:
            for i in range(l,r + 1):
                if s2[i] not in set_1:
                    break
                set_2.append(s2[i])
                     
            if sorted(set_2[::]) == sorted(set_1)[::]:
                return True
            else:    
                set_2.clear()
                l += 1
                r += 1
        return False
    
