class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} #position of each charactor in
        l = 0 #left 
        res = 0

        for r in range(len(s)): #right
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)

            mp[s[r]] = r

            res = max(res, r - l + 1)
        
        return res





