class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mp;
        
        for(int i=0;i<nums.size();i++){
            int x = nums[i];
            if(mp.find(target-x) != mp.end())
                return vector<int>{mp[target-x],i};
            mp.insert(make_pair(x,i));
        }
        return vector<int>{};
    }
};