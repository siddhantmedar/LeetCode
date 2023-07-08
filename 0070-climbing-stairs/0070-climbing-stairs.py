class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[n] = 1
        
        for i in range(len(dp)-2,-1,-1):
            dp[i] = (dp[i+1] if i+1 < len(dp) else 0) + (dp[i+2] if i+2<len(dp) else 0)

        return dp[0]