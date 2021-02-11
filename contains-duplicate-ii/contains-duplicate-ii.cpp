class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, vector<int>> m;
        for(int i=0; i<nums.size(); i++){
            m[nums[i]].push_back(i);
        }
        for(auto z: m)
        {
            for(int i=0; i<z.second.size(); i++){
                for(int j=i+1; j<z.second.size(); j++){
                    if(abs(z.second[i]-z.second[j]) <= k) return true;
                }
            }
        }
        return false;
    }
};