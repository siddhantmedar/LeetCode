class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        
        vector<int> result;
        vector<int> hash(26,0);
        vector<int> pattern_hash(26,0);
        
        int window_size = p.size();
        int string_size = s.size();
        
        if(string_size < window_size) return result;
        
        int left=0, right=0;
        
        while(right < window_size){
            pattern_hash[p[right] - 'a'] +=1;
            hash[s[right++]- 'a'] +=1;
        }
        
        right-=1;
        
        while(right < string_size){
            if(pattern_hash == hash) result.push_back(left);
            right+=1;
            if(right != string_size) hash[s[right] - 'a'] +=1;
            hash[s[left] - 'a'] -=1;
            left+=1;
        }
        return result;
    }
};