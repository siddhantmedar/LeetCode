class Solution {
public:
    bool isSubsequence(string s, string t) {
        if(s.size()==0) return true;
        
        int i = t.size()-1, j = s.size()-1;
        
        while(i>=0 and j>=0){
            if(t[i]==s[j]) j-=1;
            i-=1;
        }
        return (j<0)?true:false;
    }
};