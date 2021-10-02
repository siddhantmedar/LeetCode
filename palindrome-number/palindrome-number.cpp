class Solution {
public:
    bool isPalindrome(int x) {
        if(x==0) return true;
        int temp;
        if(x < 0){
            temp = abs(x);
        }
        else{
            temp = x;
        }
        long long reverse = 0;
        
        while(temp > 0){
            reverse = (reverse*10)+(temp%10);
            temp/=10;
        }
        if(x == reverse) return true;
        return false;
    }
};