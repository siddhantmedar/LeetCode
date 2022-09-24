class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] == "0" or (i,j) in visited:
                return
            
            visited.add((i, j))
            
            for dx, dy in directions:
                dx+=i
                dy+=j
                
                dfs(dx, dy)
                
        
        M,N = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        
        count = 0
        
        for i in range(M):
            for j in range(N):
                if (i,j) not in visited and grid[i][j] == "1":
                    dfs(i,j)
                    count+=1
        
        return count