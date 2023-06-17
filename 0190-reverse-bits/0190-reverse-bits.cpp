class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int res = 0, pos = 31;
        
        for(int i=0;i<32;i++){
            res |= (n&1)<<pos;
            
            n>>=1;
            pos-=1;
        }
        
        return res;
    }
};