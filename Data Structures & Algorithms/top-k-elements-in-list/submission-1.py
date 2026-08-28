from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for i in nums:
            dic[i] += 1

        sorted_dic = sorted(dic, key=dic.get, reverse=True)

        return sorted_dic[:k]
