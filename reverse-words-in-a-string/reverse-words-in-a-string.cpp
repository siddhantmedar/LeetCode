class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word;
        
        vector<string> v;
        
        while(ss >> word){
            v.push_back(word);
        }
        
        reverse(begin(v), end(v));
        s.clear();
        
        for(auto x: v){
            s += x;
            s += ' ';
        }
        s = s.substr(0, s.size()-1);
        return s;
    }
};