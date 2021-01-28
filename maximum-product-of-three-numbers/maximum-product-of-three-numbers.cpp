class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int product = 1;
        
        sort(nums.begin(), nums.end());
        
        product = max(nums[0]*nums[1]*nums[nums.size()-1], nums[nums.size()-3]*nums[nums.size()-2]*nums[nums.size()-1]);
        
        return product;
    }
};