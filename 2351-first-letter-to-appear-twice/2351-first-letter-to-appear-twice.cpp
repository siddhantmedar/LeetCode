class Solution {
public:
    char repeatedCharacter(string s) {
        set<char> st;
        
        char res;
        for(auto &c: s){
            if(st.find(c) != st.end()){
                res = c;
                break;
            }
            st.insert(c);
        }
        
        return res;
    }
};