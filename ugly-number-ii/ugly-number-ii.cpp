class Solution {
public:
    int nthUglyNumber(int n) {
        int result[n];  
        result[0]=1;
        int i2=0, i3=0, i5=0;
        int m2=2, m3=3, m5=5;
        
        int next_ugly=1;
        
        for(int i=1; i<n; i++){
            next_ugly = min(m2, min(m3, m5));
            result[i] = next_ugly;
            if(next_ugly == m2){
                i2++;
                m2 = result[i2]*2;
            }
            if(next_ugly == m3){
                i3++;
                m3 = result[i3]*3;
            }
            if(next_ugly == m5){
                i5++;
                m5 = result[i5]*5;
            }
        }
        
        return next_ugly;
    }
};