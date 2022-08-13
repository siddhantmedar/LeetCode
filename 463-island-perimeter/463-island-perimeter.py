class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            nonlocal count
            
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == 0:
                count+=1
                return
            
            elif grid[i][j] == "#":
                return
            
            grid[i][j] = "#"
            
            for x,y in directions:
                x+=i
                y+=j
                
                dfs(x,y)
    
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = 0
                    dfs(i,j)
                    res = max(res, count)
                    
        return res