class Solution {
public:
      static bool cmp(pair<int,string> &p1, pair<int,string> &p2){
        if(p1.first == p2.first)
            return p1.second < p2.second;
          
        return p1.first > p2.first;        
    }
    
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string,int> mp;
        
        for(auto &w: words){
            if(mp.find(w) == mp.end())
                mp[w] = 1;
            else
                mp[w]+=1;
        }
        
        vector<pair<int, string>> tmp;
        
        for(auto &t: mp){
            tmp.emplace_back(make_pair(t.second, t.first));
        }
        
        sort(begin(tmp), end(tmp), cmp);
        
        vector<string> res;
        
        for(auto &x: tmp){
            cout<<x.second <<" ";
        }
        cout<<endl;
        
        for(auto &x: tmp){
            res.emplace_back(x.second);
            k-=1;
            if(k==0) break;
        }
        
        return res;
    }
};