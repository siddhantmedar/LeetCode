class Solution {
public:
    int totalMoney(int n) {
        vector<int> dp(n+1); dp[0] = 0;
        for(int i=1; i<=n; i++){
            if(i<=7){
                dp[i] = dp[i-1]+1;
            }
            else{
                dp[i] = dp[i-7]+1;
            }
        }
        return accumulate(dp.begin(), dp.end(), 0);
    }
};
