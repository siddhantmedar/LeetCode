class Solution {
public:
    bool checkPerfectNumber(int n) {
        if(n<=0) return false;
        
        int sum = 0;
        for(int i=1;i*i<=n; i++){
            if(n%i == 0){
                sum+=i;
                if(i*i != n) sum+=n/i;
            }
        }
        return (sum-n == n)?true:false;
    }
};