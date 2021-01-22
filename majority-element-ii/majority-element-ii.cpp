class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        unordered_map<int, int> mp;
        for(int i=0; i<nums.size(); i++){
            mp[nums[i]]++;
        }
        vector<int> result;
        
        for(auto it = mp.begin(); it!=mp.end(); it++){
            if(it->second > nums.size()/3){
                result.push_back(it->first);
            }
        }
        
        return result;
    }
};
