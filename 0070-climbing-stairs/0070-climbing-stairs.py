class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(n):
            if n==0 or n==1:
                return 1
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = solve(n-1)+solve(n-2)
            
            return dp[n]
        
        
        dp = [-1]*(n+1)
        
        
        def solve2():
            dp = [0]*(n+1)
            
            dp[0]=1
            dp[1]=1
            
            for i in range(2, len(dp)):
                dp[i] = dp[i-1]+dp[i-2]
                
            return dp[n]
        
        return solve2()
        