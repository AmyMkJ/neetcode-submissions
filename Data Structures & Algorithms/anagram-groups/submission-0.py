from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        exist = defaultdict(list)
        for i in strs:
            key = tuple(sorted(i))
            exist[key].append(i)

        return list(exist.values())