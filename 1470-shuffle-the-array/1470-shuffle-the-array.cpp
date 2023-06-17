class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        int i=0;
        vector<int> res;
        
        for(int i=0; i<nums.size()/2;i++){
            res.emplace_back(nums[i]);
            res.emplace_back(nums[i+(int)nums.size()/2]);
        }
        
        return res;
    }
};