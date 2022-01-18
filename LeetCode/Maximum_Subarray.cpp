//LeetCode - Maximum Subarray Problem Solution
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxnow=INT_MIN;
        int maxprev = 0;
        for(int i=0;i<nums.size(); i++)
        {
            if(nums[i] <= maxprev + nums[i])
                maxprev += nums[i];
            else
                maxprev = nums[i];
            
            if(maxprev>maxnow)
                maxnow = maxprev;
        }        
        return maxnow;
        
    }
};
