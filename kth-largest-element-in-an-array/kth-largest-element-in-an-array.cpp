class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        sort(begin(nums), end(nums));
        reverse(begin(nums), end(nums));
        return nums[k-1];
    }
};