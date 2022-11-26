class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            q = deque([(i,j)])
            
            while q:
                n = len(q)
                
                for _ in range(n):
                    i,j = q.popleft()
                    
                    grid[i][j] = "0"
                    
                    for dx,dy in directions:
                        dx+=i
                        dy+=j
                        
                        if 0<=dx<M and 0<=dy<N and grid[dx][dy] == "1":
                            grid[dx][dy] = "0"
                            q.append((dx,dy))
                    
            
        M,N = len(grid),len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        result = 0
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    result+=1
                    bfs(i,j)
                    
        return result