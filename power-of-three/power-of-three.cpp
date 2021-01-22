class Solution {
public:
    bool isPowerOfThree(int n) {
            
        if(n == 0) return 0;
        
        if(ceil(log10(n)/log10(3)) == floor(log10(n)/log10(3))) return 1;
        else return 0;
    }
};
