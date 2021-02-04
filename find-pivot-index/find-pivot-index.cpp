class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sum = accumulate(begin(nums), end(nums), 0);
        
        int leftSum = 0;
        
        for(int i=0; i<nums.size(); i++){
            if(leftSum == sum-nums[i]-leftSum) return i;
            leftSum+=nums[i];
        }
        
        return -1;
    }
};