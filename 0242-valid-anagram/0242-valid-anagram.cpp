class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> mp;
        
        for(auto &c:s){
            auto rec = mp.find(c);
            if(rec == mp.end()){
                mp.insert(make_pair(c,1));
            }
            else{
                mp[c]+=1;
            }
        }
        
        for(auto &c:t){
            auto rec = mp.find(c);
            if(rec == mp.end()) return false;
            
            if(rec != mp.end() and mp[c] > 0){
                mp[c]-=1;
                
                if(mp[c]==0){
                    mp.erase(c);
                }
            }
        }
        
        if(mp.size() > 0){
            return false;
        }
        
        return true; 
    }
};