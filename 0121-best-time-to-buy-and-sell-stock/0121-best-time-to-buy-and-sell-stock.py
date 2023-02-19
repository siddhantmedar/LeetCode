class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        held = prices[0]
        profit = 0
        
        for ele in prices[1:]:
            if ele-held > profit:
                profit = ele-held
            elif held > ele:
                held = ele
                
        return profit