class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
        
        string mn = *min_element(begin(strs),end(strs));
        
        for(int i=0;i<mn.size();i++){
            bool valid = true;
            for(auto &x: strs){
                if(x!=mn and x[i] != mn[i])
                    valid = false;
            }
            if(valid)
                res+=mn[i];
            else
                break;
        }
        
        return res;
    }
};