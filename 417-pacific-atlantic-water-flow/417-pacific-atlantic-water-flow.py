class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        def dfs(i,j,x,y,st):
            if i<0 or j<0 or i>=M or j>=N or (i,j) in st or grid[i][j] < grid[x][y]:
                return
            
            st.add((i,j))
            
            for dx, dy in directions:
                dx+=i
                dy+=j
                
                dfs(dx,dy,i,j,st)
        
        
        M,N = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        pac, atl = set(), set()
        
        for j in range(N):
            dfs(0,j,0,j,pac)
            dfs(M-1,j,M-1,j,atl)
            
        for i in range(M):
            dfs(i,0,i,0,pac)
            dfs(i,N-1,i,N-1,atl)
        
        return atl.intersection(pac)