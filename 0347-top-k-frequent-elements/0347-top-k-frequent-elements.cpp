class Solution {
public:
    static bool cmp(pair<int,int> &a, pair<int,int> &b){
            return a.second > b.second;
        }
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        
        for(auto ele:nums){
            if(mp.find(ele)==mp.end()){
                mp.insert(pair<int,int>(ele,1));
            }
            else{
                mp[ele]+=1;
            }
        }
        
        vector<pair<int,int>> tmp;
        
        for(auto it:mp)
        {
            tmp.emplace_back(make_pair(it.first,it.second));
        }
        
        sort(begin(tmp),end(tmp),cmp);
        
        vector<int> result;
        
        for(auto x:tmp){
            if(result.size() == k){
                break;
            }
            result.emplace_back(x.first);
        }
        return result;
    }
};