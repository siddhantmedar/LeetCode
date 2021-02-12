class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0, best = INT_MIN;
        for(int i=0; i<size(nums); ++i){
            sum = max(nums[i], sum+nums[i]);
            best = max(best,sum);
        }
        return best;
    }
};