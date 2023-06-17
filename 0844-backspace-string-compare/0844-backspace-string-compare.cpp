class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char> s1, s2;
        
        for(auto &c:s){
            if(c=='#'){
                if(s1.size()>0)
                    s1.pop();
                continue;
            }
            s1.push(c);
        }
        for(auto &c:t){
            if(c=='#'){
                if(s2.size()>0)
                    s2.pop();
                continue;
            }
            s2.push(c);
        }
        
        if(s1.size()!=s2.size())
            return false;
        
        while(s1.size()>0 and s2.size()>0){
            if(s1.top()!=s2.top())
                return false;
            s1.pop(); s2.pop();
        }
        return true;
    }
};