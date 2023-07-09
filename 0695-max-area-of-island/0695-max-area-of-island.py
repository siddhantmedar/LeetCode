class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=M or j<0 or j>=N or grid[i][j] == 0:
                return
            
            visited.add((i,j))
            grid[i][j] = 0
            
            for dx,dy in dir:
                dx+=i
                dy+=j
                
                dfs(dx,dy)
                
        M,N = len(grid), len(grid[0])
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        res = 0
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    visited.clear()
                    dfs(i,j)
                    res = max(res, len(visited))
                    
        return res