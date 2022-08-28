class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(i,j):
            if i == 0:
                return j
            
            elif j == 0:
                return i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            val = 1
            
            if word1[i-1] == word2[j-1]:
                val = 0
                dp[i][j] = solve(i-1,j-1) + val
                return dp[i][j]
            
            else:
                dp[i][j] = min(solve(i,j-1),
                          solve(i-1,j-1),
                          solve(i-1,j)
                          ) + val
            
                return dp[i][j]
            
        dp = [[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        return solve(len(word1), len(word2))