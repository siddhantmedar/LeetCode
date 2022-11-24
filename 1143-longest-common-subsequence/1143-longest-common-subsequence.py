class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         def solve(m,n):
#             if m == 0 or n == 0:
#                 return 0
            
#             if dp[m][n] != -1:
#                 return dp[m][n]
            
#             if text1[m-1] == text2[n-1]:
#                 dp[m][n] = 1+solve(m-1,n-1)
#                 return dp[m][n]
            
#             else:
#                 dp[m][n] = max(solve(m-1,n), solve(m,n-1))
#                 return dp[m][n]
        
        dp = [[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    continue
                
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                    
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        
        return dp[len(text1)][len(text2)]