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
            a=1
            b=1
            
            for i in range(2, len(dp)):
                sm = a+b
                a = b
                b = sm
            
            return b
        
        return solve2()
        