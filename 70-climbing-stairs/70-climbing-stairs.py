class Solution:
    def climbStairs(self, n: int) -> int:
#         def solve(n):
#             if n == 0 or n == 1:
#                 return 1
            
#             if dp[n] != -1:
#                 return dp[n]
            
#             dp[n] = solve(n-1)+solve(n-2)
                
#             return dp[n] 
        
#         dp = [-1 for i in range(n+1)]
        
#         return solve(n)

        dp = [0 for i in range(n+1)]
        dp[0], dp[1] = 1, 1
        
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[len(dp)-1]