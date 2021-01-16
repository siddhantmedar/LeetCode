class Solution {
public:
    int missingNumber(vector<int>& nums) {
        if(nums.size() == 0) return 1;
        
        int missing = nums.size();
        for(int i=0; i<nums.size(); i++){
            missing^=i^nums[i];
        }
        return missing;
    }
};
