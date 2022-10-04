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
                
        
        def bfs():
            src = grid[sr][sc]
            fill = color
            
            q = deque([(sr,sc)])
            grid[sr][sc] = fill
            
            while q:
                n = len(q)
                
                for k in range(n):
                    i,j = q.popleft()

                    for dx, dy in directions:
                        dx+=i
                        dy+=j
                        
                        if 0<=dx<M and 0<=dy<N and grid[dx][dy] == src and grid[dx][dy] != fill:
                            grid[dx][dy] = fill
                            q.append((dx,dy))
            
        
        M,N = len(grid), len(grid[0])
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        # dfs(sr, sc, grid[sr][sc], color)
        bfs()
        
        return grid