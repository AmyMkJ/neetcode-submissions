class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = []
        for i in range(len(nums)):
            if nums[i] in exist:
                return True
            exist.append(nums[i])

        return False