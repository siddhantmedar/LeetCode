class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        stock = nums[0]
        profit = 0
        
        for ele in nums[1:]:
            if ele < stock:
                stock = ele                
            else:
                profit = max(profit, ele-stock)
        
        return profit