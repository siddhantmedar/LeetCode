class Solution {
    int minLength(vector<string>& strs){
        int min = strs[0].size();
        for(int i=1; i<strs.size(); ++i){
            if(strs[i].size() < min) min = strs[i].size();
        }
        return min;
    }
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0) return "";
        int min = minLength(strs);
        
        char current;
        
        string result = "";
        
        for(int i=0; i<min; i++){
            current = strs[0][i];
            
            for(int j=1;j<strs.size(); j++){
                if(current != strs[j][i]) return result;
            }
            
            result.push_back(current);
        }
        
        return result;
    }
};