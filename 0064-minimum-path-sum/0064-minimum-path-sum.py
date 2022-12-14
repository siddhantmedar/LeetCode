class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def solve(i,j):
            if i<0 or i>=M or j<0 or j>=N:
                return float("inf")
            
            if (i,j)==(M-1,N-1):
                return grid[i][j]
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = min(solve(i,j+1),solve(i+1,j))+grid[i][j]
            
            return dp[i][j]
        
        
        M,N = len(grid),len(grid[0])
        
        dp = [[-1]*N for _ in range(M)]
        
        return solve(0,0)