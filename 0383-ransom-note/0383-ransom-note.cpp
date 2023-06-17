class Solution {
public:
    bool canConstruct(string r, string m) {
        unordered_map<char,int> mp;
        
        for(auto x: m){
            if(mp.find(x) == mp.end()){
                mp[x]=1;
            }
            else
                mp[x]+=1;
        }
        
        for(auto x:r){
            if(mp.find(x)!=mp.end()){
                mp[x]-=1;
                if(mp[x]==0)
                    mp.erase(x);
            }
            else
                return false;
        }
        return true;
    }
};