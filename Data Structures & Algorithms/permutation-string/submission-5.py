from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        s1 = Counter(s1)

        for l in range(len(s2) - r + 1):
            new = Counter(s2[l:l+r])

            if new == s1:
                return True

        return False


