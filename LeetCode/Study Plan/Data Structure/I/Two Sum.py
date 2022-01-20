class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for cnt, num in enumerate(nums):
            if target - num in lookup:
                return lookup[target-num], cnt
            lookup[num] = cnt
