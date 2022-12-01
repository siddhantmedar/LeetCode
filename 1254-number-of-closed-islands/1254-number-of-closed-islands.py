class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=M or j<0 or j>=N or (i,j) in visited or grid[i][j]==1:
                return
            
            visited.add((i,j))
            
            for dx,dy in directions:
                dx+=i
                dy+=j
                
                dfs(dx,dy)
            
        
        M,N = len(grid),len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        visited = set()
        cnt = 0
        
        for j in range(N):
            if (0,j) not in visited and grid[0][j] == 0:
                dfs(0,j)
            if (M-1,j) not in visited and grid[M-1][j] == 0:
                dfs(M-1,j)
        
        for i in range(M):
            if (i,0) not in visited and grid[i][0] == 0:
                dfs(i,0)
            if (i,N-1) not in visited and grid[i][N-1] == 0:
                dfs(i,N-1)
        
        for i in range(M):
            for j in range(N):
                if (i,j) not in visited and grid[i][j]==0:
                    dfs(i,j)
                    cnt+=1
                        
        return cnt
    
    
# [[0,0,1,1,0,1,0,0,1,0]
#  [1,1,0,1,1,0,1,1,1,0]
#  [1,0,1,1,1,0,0,1,1,0]
#  [0,1,1,0,0,0,0,1,0,1]
#  [0,0,0,0,0,0,1,1,1,0]
#  [0,1,0,1,0,1,0,1,1,1]
#  [1,0,1,0,1,1,0,0,0,1]
#  [1,1,1,1,1,1,0,0,0,0]
#  [1,1,1,0,0,1,0,1,0,1]
#  [1,1,1,0,1,1,0,1,1,0]]