class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        vector<int> left(nums.size(),0),right(nums.size(),0);
        left[0] = nums[0]; right[right.size()-1] = nums[right.size()-1];
        
        for(int i=1;i<left.size();i++){
            left[i] = nums[i]+left[i-1];
        }
        
        for(int i=right.size()-2;i>=0;i--){
            right[i] = right[i+1]+nums[i];
        }
        
        for(int i=0;i<left.size();i++){
            if(left[i]==right[i]) return i;
        }
        
        return -1;
    }
};