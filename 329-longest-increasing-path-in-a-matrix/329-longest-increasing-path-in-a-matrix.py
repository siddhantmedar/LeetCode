class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or j<0 or i>=M or j>=N:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            result = 0
            
            for dx, dy in directions:
                dx+=i
                dy+=j
                
                if 0<=dx<M and 0<=dy<N and grid[dx][dy] > grid[i][j]:
                    result = max(result, dfs(dx,dy))
            
            dp[i][j] = max(dp[i][j], result+1)
            
            return dp[i][j]
        
        
        M,N = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        dp = [[-1 for _ in range(N)] for _ in range(M)]
        
        result = 0
        
        for i in range(M):
            for j in range(N):
                result = max(result, dfs(i,j))
                
        return result