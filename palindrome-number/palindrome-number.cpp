class Solution {
public:
    bool isPalindrome(int x) {
        string temp = to_string(x);
        if(temp.size() == 0 || temp.size() == 1) return true;
        int low=0, end=temp.size()-1;
        while(low<end){
            if(temp[low] != temp[end]) return false;
            low++;end--;
        }
        return true;
    }
};