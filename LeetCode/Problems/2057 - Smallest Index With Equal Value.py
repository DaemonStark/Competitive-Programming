class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        flag = 0
        ans = sys.maxsize
        for i in range(len(nums)):
            if i%10 == nums[i]:
                ans = min(i, ans)
                flag = 1
        
        if flag==1:
            return ans
        else:
            return -1
        
