class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& nums) {
        if(nums.size()<=1) return nums;
        vector<vector<int>> result;
        sort(begin(nums), end(nums));
        result.push_back(nums[0]);
        
        for(int i=1; i<nums.size(); i++){
            if(result.back()[1]>=nums[i][0]) result.back()[1] = max(result.back()[1], nums[i][1]);
            else result.push_back(nums[i]);
        }
        return result;
    }
};