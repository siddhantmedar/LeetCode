class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> st;
        int cnt = 0;
        
        for(auto x: emails){
            stringstream ss(x);
            string word;
            
            vector<string> tmp;
            
            while(getline(ss,word,'@')){
                tmp.emplace_back(word);
            }

            string local = tmp[0], domain = tmp[1];
            
            word.clear();
            stringstream ss1(local);
            tmp.clear();
            
            while(getline(ss1,word,'+')){
                tmp.emplace_back(word);
            }

            local = tmp[0];
            
            word.clear();
            stringstream ss2(local);
            tmp.clear();
            
            while(getline(ss2,word,'.')){
                tmp.emplace_back(word);
            }

            local = "";
            
            for(auto z: tmp){
                local+=z;
            }
            
            string mail = local+"@"+domain;
            
            if(st.find(mail)==st.end())
                cnt+=1;
                st.insert(mail);
        }
        
        return cnt;
    }
};