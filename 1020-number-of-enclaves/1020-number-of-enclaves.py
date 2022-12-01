class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(i,j):
            visited.add((i,j))
            
            q = deque([(i,j)])
            
            while q:
                n = len(q)
                
                for _ in range(n):
                    i,j = q.popleft()
                    
                    for dx,dy in directions:
                        dx+=i
                        dy+=j
                            
                        if dx<0 or dx>=M or dy<0 or dy>=N or (dx,dy) in visited or grid[dx][dy]==0:
                            continue
                        
                        visited.add((dx,dy))
                        q.append((dx,dy))
        
        
        M,N = len(grid),len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        visited = set()
        cnt = 0
        
        for j in range(N):
            if (0,j) not in visited and grid[0][j] == 1:
                bfs(0,j)
            if (M-1,j) not in visited and grid[M-1][j] == 1:
                bfs(M-1,j)
        
        for i in range(M):
            if (i,0) not in visited and grid[i][0] == 1:
                bfs(i,0)
            if (i,N-1) not in visited and grid[i][N-1] == 1:
                bfs(i,N-1)
        
        for i in range(M):
            for j in range(N):
                if (i,j) not in visited and grid[i][j]==1:
                    cnt+=1
            
        return cnt