class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        int start=0, end = s.size()-1;
        while(start<end){
            if(s[start] != s[end]){
                return false;
            }
            start++; end--;
        }
        return true;
    }
};
