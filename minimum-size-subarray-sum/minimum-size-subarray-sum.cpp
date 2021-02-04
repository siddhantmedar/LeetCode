class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int answer = INT_MAX;
        int left = 0;
        int sum = 0;
        
        for(int i=0; i<n; i++){
            sum += nums[i];
            while(sum>=target){
                answer = min(answer, i+1-left);
                sum-=nums[left++];
            }
        }
        
        return (answer != INT_MAX) ? answer:0;
    }
};