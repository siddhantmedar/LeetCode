class Solution {
public:
    int helperFunction(int n){
        int count = 0;
        
        while(n>0){
            n=n&(n-1);
            count++;
        }
        return count;
    }
    vector<int> countBits(int num) {
        
        vector<int> v;
        
       for(int i=0; i<=num; i++){
            v.push_back(helperFunction(i));
       }
        
        return v;
    }
};
