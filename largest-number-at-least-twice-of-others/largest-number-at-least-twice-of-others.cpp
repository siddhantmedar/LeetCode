class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        
        int maxElementIndex = max_element(nums.begin(), nums.end()) - nums.begin();
        
        for(int i=0; i<nums.size(); i++){
            if(maxElementIndex != i && nums[maxElementIndex] < 2*nums[i]){
                return -1;
            }
        }
        return maxElementIndex;
    }
};