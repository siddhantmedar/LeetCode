class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i,j,price in prices:
            dp[i][j] = price
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                for cut in range(1,j//2+1):
                    dp[i][j] = max(dp[i][j],dp[i][cut]+dp[i][j-cut])
                    
                for cut in range(1,i//2+1):
                    dp[i][j] = max(dp[i][j],dp[cut][j]+dp[i-cut][j])
        
        return dp[m][n]