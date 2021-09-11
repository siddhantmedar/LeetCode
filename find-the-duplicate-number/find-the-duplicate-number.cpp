class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int result;
        for(int i=0; i<nums.size(); ++i){
            if(nums[abs(nums[i])] >= 0) nums[abs(nums[i])] = -nums[abs(nums[i])];
            else{
                result = abs(nums[i]);
                break;
            }
        }
        return result;
    }
};