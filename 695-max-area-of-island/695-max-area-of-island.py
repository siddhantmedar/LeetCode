class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            count = 1
            
            for x,y in directions:
                count+=dfs(x+i,y+j)
                
            return count
        
        m,n = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))
                
        return res