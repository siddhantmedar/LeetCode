class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = prices[0]
        
        profit = 0
        
        for price in prices[1:]:
            if price >= stock:
                profit = max(profit, price-stock)
                
            else:
                if price < stock:
                    stock = price
                    
        return profit