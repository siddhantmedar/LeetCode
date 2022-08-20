class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        profit, mn = float("-inf"), float("inf")
        
        for i in range(len(nums)):
            curr = nums[i]
            if curr > mn:
                profit = max(profit, curr-mn)
                
            mn = min(mn, curr)
            
        return profit if profit != float("-inf") else -1