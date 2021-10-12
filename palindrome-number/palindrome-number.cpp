class Solution {
public:
    bool isPalindrome(int x) {
        long temp = abs(x);
        long  rev = 0;

        while(temp > 0){
            rev =(rev*10)+(temp%10);
            temp/=10;
        }
        return x == rev;
    }
};