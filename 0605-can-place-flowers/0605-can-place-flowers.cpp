class Solution {
public:
    bool canPlaceFlowers(vector<int>& v, int n) {
        vector<int> tmp;
        tmp.emplace_back(0);
        for(auto x: v){
            tmp.emplace_back(x);
        }
        tmp.emplace_back(0);
        
        for(int i=1;i<tmp.size()-1;i++){
            if(tmp[i]==0 and tmp[i-1]==0 and tmp[i+1]==0){
                tmp[i]=1;
                n-=1;
            }
        }
        return n<=0;
    }
};