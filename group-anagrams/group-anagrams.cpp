class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int size = strs.size();
        
        vector<vector<string>> result;
        
        unordered_map<string, vector<string>> m;
        
        for(int i=0; i<size; i++){
            string temp = strs[i];
            sort(begin(temp), end(temp));
            
            if(m.find(temp) == m.end()){
                vector<string> v;
                v.push_back(strs[i]);
                m[temp] = v;
            }
            else{
                m[temp].push_back(strs[i]);
            }
        }
        
        for(auto& x: m){
            result.push_back(x.second);
        }
        
        return result;
    }
};