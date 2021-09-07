class Solution {
public:
    int lengthOfLastWord(string str) {
        stringstream s(str);
        string temp;
        
        while(s>>temp){
        }
        return temp.size();
    }
};