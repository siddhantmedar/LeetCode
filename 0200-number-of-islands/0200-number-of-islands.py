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
                        
                        if dx<0 or dx>=M or dy<0 or dy>=N or grid[dx][dy] == "0":
                            continue
                        grid[dx][dy] = "0"
                        q.append((dx,dy))
        
            
        M,N = len(grid),len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        cnt = 0
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    bfs(i,j)
                    cnt+=1
                    
        return cnt