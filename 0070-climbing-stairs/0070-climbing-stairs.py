class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(n):
            if n<2:
                return 1
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = solve(n-1)+solve(n-2)
            
            return dp[n]
        
        
        dp = [-1 for i in range(n+1)]
        
        return solve(n)