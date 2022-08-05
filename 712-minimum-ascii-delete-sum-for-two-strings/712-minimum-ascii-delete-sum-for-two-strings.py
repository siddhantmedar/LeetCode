class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==0 and j==0:
                    dp[i][j] = 0 
                
                elif i==0:
                    dp[i][j] = dp[i][j-1] + ord(s2[j-1])
                
                elif j==0:
                    dp[i][j] = dp[i-1][j] + ord(s1[i-1])
                    
                else:
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    
                    else:
                        dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]),
                                      dp[i][j-1] + ord(s2[j-1]))
        
        return dp[len(dp)-1][len(dp[0])-1]