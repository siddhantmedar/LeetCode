class Solution {
public:
     static bool cmp(pair<int,int> &p1, pair<int,int> &p2){
        if(p1.first == p2.first)
            return p1.second < p2.second;
          
        return p1.first > p2.first;        
    }
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        
        for(auto &w: nums){
            if(mp.find(w) == mp.end())
                mp[w] = 1;
            else
                mp[w]+=1;
        }
        
        vector<pair<int, int>> tmp;
        
        for(auto &t: mp){
            tmp.emplace_back(make_pair(t.second, t.first));
        }
        
        sort(begin(tmp), end(tmp), cmp);
        
        vector<int> res;
        
        for(auto &x: tmp){
            res.emplace_back(x.second);
            k-=1;
            if(k==0) break;
        }
        
        return res;
    }
};