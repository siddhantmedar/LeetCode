class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        
        mx = 0
        
        for i in range(len(nums)):
            mx = max(mx + nums[i], nums[i])
            
            result = max(mx, result)
            
        return result
        