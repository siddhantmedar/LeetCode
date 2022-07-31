class Solution:
    def maximalSquare(self, nums: List[List[str]]) -> int:
        m,n = len(nums), len(nums[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        res = 0
        
        for i in range(m-1, -1,-1):
            for j in range(n-1,-1,-1):
                if (i == m-1 or j == n-1):
                    dp[i][j] = int(nums[i][j])
                    
                elif nums[i][j] == "0":
                    dp[i][j] = 0
                    
                else:
                    dp[i][j] = min(dp[i][j+1],dp[i+1][j+1],dp[i+1][j])+1
                
                res = max(res, dp[i][j])
        
        return res**2
        