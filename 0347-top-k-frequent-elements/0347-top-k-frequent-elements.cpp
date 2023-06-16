class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        
        for(auto x:nums){
            if(mp.find(x)==mp.end())
                mp[x]=1;
            else
                mp[x]+=1;
        }
        
        vector<vector<int>> v(nums.size()+1);
        
        for(auto x:mp){
            v[x.second].emplace_back(x.first);
        }
        
        vector<int> res;
        
        int i = v.size()-1;
        
        while(i>=0){
            if(k==0) break;
            if(v[i].size() > 0){
                for(auto x:v[i]){
                    if(k>0){
                        res.emplace_back(x);
                        k-=1;
                    }
                }
            }
            i-=1;
        }
        
        return res;
        
    }
};