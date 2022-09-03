class Solution:
    def trap(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = [0]*n, [0]*n
        
        left[0] = nums[0]
        right[n-1] = nums[n-1]
        
        for i in range(1, n):
            left[i] = max(left[i-1], nums[i])
        
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], nums[i])
            
        res = 0
        
        for i in range(n):
            res+=min(left[i], right[i]) - nums[i]
            
        return res