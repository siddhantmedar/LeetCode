class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        
        n = len(nums)
        
        if n % 2:
            median = nums[n // 2]
            
        elif n % 2 == 0:
            idx = n // 2
            median = (nums[idx-1]+nums[idx]) // 2
            
        res = 0
        
        for ele in nums:
            res+=abs(median-ele)
            
        return res