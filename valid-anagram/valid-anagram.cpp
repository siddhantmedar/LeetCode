class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<char> vs, vt;
        for(char temp:s) vs.push_back(temp);
        for(char temp:t) vt.push_back(temp);
        
        sort(begin(vs), end(vs));
        sort(begin(vt), end(vt));
        
        return vs == vt? true:false;
    }
};