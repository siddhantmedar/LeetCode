class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] - stock > profit:
                profit = prices[i] - stock
            else:
                stock = min(stock, prices[i])
                
        return profit
        