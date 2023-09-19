class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        buy = prices[0]
        
        for ele in prices[1:]:
            if ele-buy>0:
                profit = max(profit,ele-buy)
            else:
                buy = min(buy,ele)
                
        return profit