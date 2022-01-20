//LeetCode - Contains Duplicate - Problem Solution in C++

#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if(nums.empty() == true)
            return false;
        int n = nums.size();
        unordered_set<int> s;
        int  i=0;
        while(i<n)
        {
            s.insert(nums[i]);
            i++;
        }
        
        return (s.size() != nums.size());
        
    }
};
