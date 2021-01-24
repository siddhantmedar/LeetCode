class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        unordered_map <int, int> mp;
              
        for(int i=0; i<nums.size(); i++){
            mp[nums[i]]++;
        }
        
        int result;
        
        for(auto it = mp.begin(); it!=mp.end(); it++){
            if(it->second > 1) result = it->first;
        }
        
        return result;
    }
};
