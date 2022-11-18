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
        
        def solve2():
            n = len(nums)
            dp = [-1 for i in range(n)]
            
            dp[n-1] = nums[n-1]
            
            for i in range(len(dp)-2,-1,-1):
                exclude = dp[i+1]
                include = dp[i+2] if i+2 < len(dp) else 0
                include += nums[i]
                
                dp[i] = max(include, exclude)
            
            return dp[0]
        
        return solve2()