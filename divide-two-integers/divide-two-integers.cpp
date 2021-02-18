class Solution {
public:
    int divide(int dividend, int divisor) {
        if(dividend == INT_MIN and divisor == -1) return INT_MAX;
        if(dividend == INT_MIN and divisor == 1) return INT_MIN;
        int quotient = 0;
        int sign= (dividend < 0) ^ (divisor < 0) ? -1:1;
        dividend = dividend > 0? -dividend:dividend;
        divisor = (divisor > 0)? -divisor:divisor;
        while(dividend <= divisor){
            int i=1, acc =divisor;
            while(acc > INT_MIN>>1 and dividend <= acc+acc){
                i+=i; acc+=acc;
            }
            dividend -= acc;
            quotient += i;
        }
        return sign*quotient;
    }
};