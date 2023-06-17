class Solution {
public:
    long reverse(long x) {
        bool neg = false;
        
        if(x<0){
            neg = true;
            x*=-1;
        }
        
        long res = 0;
        
        while(x>0){
            res = res*10+(x%10);
            x/=10;
        }
        
        if((res > pow(2,31)-1) or (res <= pow(-2,31)))
            res = 0;
        return neg?-1*res:res;
        
    }
};