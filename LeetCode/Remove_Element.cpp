// Leetcode - Remove Element Solution
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int a = 0, s = nums.size();
        while(a<s){
            if(nums[a]!=val)
                ++a;
            else
                swap(nums[a], nums[--s]);
                
        }
        return s;
    }
};
