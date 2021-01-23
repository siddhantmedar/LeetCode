class Solution {
public:
    string removeKdigits(string str, int k) {
        
        if(k == 0) return str;
        
        if(str.size() <= k){
            return "0";
        }
        
        for(int i=0; i<k; i++){
            int j=0;
            while(j < str.size()-1 && str[j] <= str[j+1]){
                j++;
            }
            str.erase(str.begin()+j, str.begin()+j+1);
        }
        
        while(str.size()>0 and str[0] == '0'){
            str.erase(str.begin(), str.begin()+1);
        }
        
        if(str.size() == 0) return "0";
        return str;
    }
};
