class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def solve(m,n):
            if m == 0 or n == 0:
                return 0
            
            if dp[m][n] != -1:
                return dp[m][n]
            
            if text1[m-1] == text2[n-1]:
                dp[m][n] = 1+solve(m-1,n-1)
                return dp[m][n]
            
            else:
                dp[m][n] = max(solve(m-1,n), solve(m,n-1))
                return dp[m][n]
        
        dp = [[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        return solve(len(text1),len(text2))