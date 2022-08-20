class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, mn = 0, prices[0]
        
        for i in range(1, len(prices)):
            curr = prices[i]
            
            if curr < mn:
                mn = curr
                
            else:
                profit = max(profit, curr-mn)
                
        return profit