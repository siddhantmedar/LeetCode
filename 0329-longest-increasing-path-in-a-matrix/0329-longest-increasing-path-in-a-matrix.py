class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        def dfs(i,j,pre):
            if i<0 or i>=M or j<0 or j>=N or (i,j) in visited:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            cnt = 1
            visited.add((i,j))
            
            for dx,dy in dir:
                dx+=i
                dy+=j
                if 0<=dx<M and 0<=dy<N and grid[dx][dy] > grid[i][j]:
                    cnt = max(cnt, dfs(dx,dy,grid[i][j]) + 1)
            
            visited.remove((i,j))
            dp[i][j] = cnt
            
            return dp[i][j]
            
        M,N = len(grid), len(grid[0])
        dp = [[-1 for _ in range(N)] for _ in range(M)]
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        res = 0
        
        for i in range(M):
            for j in range(N):
                    res = max(res, dfs(i,j,None))
                    
        return res