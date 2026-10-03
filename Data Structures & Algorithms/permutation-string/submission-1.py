class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        l = 0
        s1 = sorted(s1)

        for l in range(len(s2)):
            if s2[l] in s1:
                new = sorted(s2[l:r+l])

                if new == s1:
                    return True

        return False


