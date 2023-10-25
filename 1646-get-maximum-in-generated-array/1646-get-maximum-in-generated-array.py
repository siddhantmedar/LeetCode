class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        
        mx = float("-inf")
        
        nums = [0]*(n+1)
        nums[1] = 1
        
        for i in range(2,n+1):
            idx = i//2 if i%2==0 else (i-1)//2
            
            if i%2==0:
                nums[i] = nums[idx]
                
            else:
                nums[i] = nums[idx]+nums[idx+1]
                
            mx = max(mx, nums[i])
            
        return mx
                
        