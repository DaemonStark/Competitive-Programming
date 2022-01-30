# LeetCode - Keep Multiplying Found Values by Two Solution

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        mp = {}
        for i in nums:
            mp[i] = mp.get(i, 0) + 1

        for i in range(len(nums)):
            if original in mp.keys():
                original *= 2
        
        return original
