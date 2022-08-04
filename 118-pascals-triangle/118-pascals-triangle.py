class Solution:
    def generate(self, n: int) -> List[List[int]]:
        dp = [[0]*i for i in range(1, n+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i==0 and j==0:
                    dp[i][j] = 1
                    
                elif i==0 or j==0:
                    dp[i][j] = dp[i-1][j]
                    
                else:
                    first = dp[i-1][j-1] if j-1 < len(dp[i-1]) else 0
                    second = dp[i-1][j] if j < len(dp[i-1]) else 0
                    
                    dp[i][j] = first+second
                    
        return dp