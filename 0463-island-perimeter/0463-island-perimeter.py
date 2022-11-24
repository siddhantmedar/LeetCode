class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if (i,j) in visited:
                return 0
            
            if i<0 or i>=M or j<0 or j>=N or grid[i][j] == 0:
                return 1
            
            visited.add((i,j))
            
            cnt = 0
            
            for dx,dy in directions:
                dx+=i
                dy+=j
                
                cnt+=dfs(dx,dy)
                
            return cnt
        
        
        M,N = len(grid),len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        
        result = 0
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    result = max(result, dfs(i,j))
                    
        return result