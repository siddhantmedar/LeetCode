class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            
            for x,y in directions:
                x+=i
                y+=j
                
                dfs(x,y)
                    
        m,n = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count+=1
                    
        return count