class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            if i<0 or i>=M or j<0 or j>=N or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            
            for dx,dy in dir:
                dx+=i 
                dy+=j
                
                dfs(dx,dy)
                
        M,N = len(grid), len(grid[0])
        cnt = 0
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    cnt+=1
                    dfs(i,j)
        
        return cnt