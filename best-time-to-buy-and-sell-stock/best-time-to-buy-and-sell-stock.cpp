class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 0|| prices.size()<=1) return 0;
         int result = 0, min=prices[0];
        for(int i=1; i<prices.size(); i++){
                if(prices[i]<min){
                    min = prices[i];
                }
            else{
                result = max(result, prices[i]-min);
                }
        }
        return result;
    }
};
