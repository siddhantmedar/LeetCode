class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        
        for(auto &x: strs){
            string tmp = x;
            sort(begin(tmp),end(tmp));
            mp[tmp].emplace_back(x);
        }
        
        vector<vector<string>> res;
        
        for(auto &x: mp){
            res.emplace_back(x.second);
        }
        
        return res;
    }
};