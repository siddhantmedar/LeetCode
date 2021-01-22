class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int majority_index = 0, count = 1;
        for(int i=1; i<nums.size(); i++){
            if(nums[majority_index] == nums[i]) count++;
            else count--;
            if(count == 0){
                majority_index = i, count=1;
            }
        }
        return nums[majority_index];
        
    }
};
