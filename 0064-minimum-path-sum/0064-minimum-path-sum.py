class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def solve2():
            dp = [[0]*N for _ in range(M)]
            
            dp[M-1][N-1] = grid[M-1][N-1]
            
            for i in range(M-1,-1,-1):
                for j in range(N-1,-1,-1):
                    if (i,j) == (M-1,N-1):
                        continue
                    
                    right = dp[i][j+1] if j+1<len(dp[0]) else float("inf")
                    down = dp[i+1][j] if i+1<len(dp) else float("inf")
                    
                    dp[i][j] = min(right,down)+grid[i][j]
                    
            return dp[0][0]
        
        
        M,N = len(grid),len(grid[0])
        
        return solve2()