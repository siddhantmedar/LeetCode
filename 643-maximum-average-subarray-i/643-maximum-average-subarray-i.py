class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float("-inf")
        
        sm = 0
        
        for i in range(k):
            sm+=nums[i]
            
        res = max(res, sm/k)
        
        for i in range(k, len(nums)):
            sm-=nums[i-k]
            sm+=nums[i]
            
            res = max(res, sm/k)
            
        return res