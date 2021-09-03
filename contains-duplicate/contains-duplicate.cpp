class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        sort(begin(nums), end(nums));
        int flag = 0;
        for(int i=0; i<nums.size()-1; ++i){
            if(nums[i] == nums[i+1]){
                flag=1; break;
            }
        }
        if(flag) return true;
        else return false;
    }
};