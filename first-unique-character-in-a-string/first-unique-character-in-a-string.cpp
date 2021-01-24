class Solution {
public:
    int firstUniqChar(string s) {
        map<char, int> m;
        
        for(int i=0; i<s.size(); i++){
            m[s[i]]++;
        }
        
        for(int i=0 ; i<s.size(); i++){
            for(auto it: m){
                if(it.first == s[i] && it.second == 1) return i;
            }
        }
        
        return -1;
    }
};
