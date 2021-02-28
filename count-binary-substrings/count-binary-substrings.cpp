class Solution {
public:
    int countBinarySubstrings(string s) {
        int result = 0;
        int current=1, previous=0;
        for(int i=1;i<s.size(); i++){
            if(s[i] != s[i-1]){
                result += min(current, previous);
                previous = current;
                current = 1;
            }
            else current++;
        }
        return result + min(previous, current);
    }
    
};