class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        if(nums.size() == 0) return nums;
        
        vector<int> result;
        int temp=0;
        
        for(int i=0; i<nums.size(); i++){
            result.emplace_back(temp+nums[i]);
            temp+=nums[i];
        }
        
        return result;
        
    }
};