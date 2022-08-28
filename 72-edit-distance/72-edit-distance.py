class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
#         def solve(i,j):
#             if i == 0:
#                 return j
            
#             elif j == 0:
#                 return i
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             val = 1
            
#             if word1[i-1] == word2[j-1]:
#                 val = 0
#                 dp[i][j] = solve(i-1,j-1) + val
#                 return dp[i][j]
            
#             else:
#                 dp[i][j] = min(solve(i,j-1),
#                           solve(i-1,j-1),
#                           solve(i-1,j)
#                           ) + val
            
#                 return dp[i][j]
            
#         dp = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
#         return solve(len(word1), len(word2))
    
        dp = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                    
                else:
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = min(dp[i-1][j-1],
                                      dp[i][j-1],
                                      dp[i-1][j]) + 1
                       
        return dp[len(dp)-1][len(dp[0])-1]