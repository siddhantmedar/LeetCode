class Solution {
public:
    vector<int> plusOne(vector<int>& nums) {
        int carry = 1;
        
        for(int i = nums.size()-1; i>=0; i--){
            int sum = nums[i]+carry;
            
            if(sum>=10) carry = 1;
            else carry = 0;
            nums[i] = sum%10;
        }
        
        if(carry){
            vector<int> result;
            result.push_back(1);
            for(auto v: nums)
                result.push_back(v);
            return result;
        }
        else return nums;
    }
};