class NumArray {
public:
    vector<int> res;
    NumArray(vector<int>& nums) {
        res.resize(nums.size());
        res[0] = nums[0];
        res.emplace_back(nums[0]);
        
        for(int i=1;i<nums.size();i++){
            res[i] = res[i-1]+nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        if(left==0)
            return res[right];
        return res[right]-res[left-1];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */