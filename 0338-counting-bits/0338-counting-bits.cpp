class Solution {
public:
    int count(int n){
        int cnt = 0;
        
        for(int i=0;i<32;i++){
            cnt+=(n&1);
            n>>=1;
        }
        
        return cnt;
    }
    
    vector<int> countBits(int n) {
        vector<int> res;
        
        for(int i=0;i<=n;i++){
            res.emplace_back(count(i));
        }
        
        return res;
    }
};