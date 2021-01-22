class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n == 0) return 0;
        
        if(ceil(log10(n)/log10(4)) == floor(log10(n)/log10(4))) return 1;
        else return 0;
    }
};
