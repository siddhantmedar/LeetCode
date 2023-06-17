class Solution {
public:
    vector<int> addToArrayForm(vector<int>& nums, int k) {
        int carry = 0;
        
        for(int i=nums.size()-1;i>=0;i--){
            int total = nums[i]+(k%10)+carry;
            k = k/10;
            nums[i] = total%10;
            carry = total/10;
        }
        while (k or carry){
            int total = (k%10)+carry;
            k/=10;
            carry = total/10;
            nums.insert(nums.begin(),total%10);
        }
        
        return nums;
    }
};