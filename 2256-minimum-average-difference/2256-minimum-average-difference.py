class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sm = 0
        
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        sm = nums[0]
        
        res = None
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]+nums[i]
            sm+=nums[i]
        
        mn = float("inf")
        
        for i in range(len(nums)):
            left = prefix[i] // (i+1)
            
            num = sm-prefix[i]
            den = len(nums)-i-1
            if num == 0:
                right = 0
            else:
                right = num // den
            
            if mn > abs(left - right):
                mn = abs(left-right)
                res = i
        
        return res
        
        # 2 | 5  3  9  5  3
        # 2   7 10 19 24 27
        
        
        0/(6-5-1)