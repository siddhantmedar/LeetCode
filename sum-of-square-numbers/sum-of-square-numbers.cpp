class Solution {
public:
    bool judgeSquareSum(int c) {
        unordered_map<long long,int> m;
        
        for(long long i=0; i*i<=c; i++){
            m[i*i]++;
            if(m.count(c-i*i)) return true;
        }
        return false;
    }
};