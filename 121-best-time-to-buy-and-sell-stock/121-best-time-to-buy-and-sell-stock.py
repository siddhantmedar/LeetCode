class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = prices[0]
        
        profit = 0
        
        for ele in prices[1:]:
            if ele >= stock:
                profit = max(profit, ele-stock)
                
            else:
                stock = min(stock, ele)
                
        return profit