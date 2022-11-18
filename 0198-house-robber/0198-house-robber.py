class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(idx):
            if idx>=len(nums):
                if idx == len(nums)-1:
                    return nums[idx]
                
                return 0
            
            if dp[idx] != -1:
                return dp[idx]
            
            exclude = solve(idx+1)
            include = solve(idx+2)+nums[idx]
            
            dp[idx] = max(include, exclude)
            
            return dp[idx]
        
        
        dp = [-1 for i in range(len(nums)+1)]
        
        return solve(0)