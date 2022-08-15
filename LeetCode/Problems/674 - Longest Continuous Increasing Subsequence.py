class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if(len(nums)==0):
            return 0
        size = 1
        ans = 1
        for i in range(1,len(nums)):
            if(nums[i]>nums[i-1]):
                size+=1
                ans = max(size, ans)
            else:
                size=1
            
        return ans
    
