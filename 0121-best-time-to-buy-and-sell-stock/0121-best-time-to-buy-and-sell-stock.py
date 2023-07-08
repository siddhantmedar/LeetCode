class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        
        for i,sell in enumerate(prices[1:]):
            if sell > buy:
                res = max(res, sell-buy)
            else:
                buy = min(buy, sell)
                
        return res