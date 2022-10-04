class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i, j, src, fill):
            if i<0 or j<0 or i>=M or j>=N or grid[i][j] != src or grid[i][j] == fill:
                return
            
            grid[i][j] = fill
            
            for dx, dy in directions:
                dx+=i
                dy+=j
                
                dfs(dx,dy,src,fill)
            
        
        M,N = len(grid), len(grid[0])
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        dfs(sr, sc, grid[sr][sc], color)
        
        return grid
    
    
    
#      [0,0,0]
#      [2,2,2]
# 1
# 0
# 2