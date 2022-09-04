class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i,j,x,y):
            if i<0 or i>=M or j<0 or j>=N or grid[i][j] == 0:
                return
            
            pos.add((i-x, j-y))
            grid[i][j] = 0
            
            for dx,dy in directions:
                dfs(dx+i, dy+j, x, y)
        
        M,N = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        st = set()
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    pos = set()
                    dfs(i,j,i,j)
                    st.add(frozenset(pos))
        
        return len(st)