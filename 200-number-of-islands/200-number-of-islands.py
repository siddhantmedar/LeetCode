class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=M or j<0 or j>=N or (i,j) in visited or grid[i][j] == "0":
                return False
            
            visited.add((i,j))
            
            for dx, dy in directions:
                dx+=i
                dy+=j
                
                dfs(dx, dy)
        
        M,N = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        
        count = 0
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i,j)
                    count+=1
                    
        return count