class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i,j):
            q = deque([(i,j)])
            visited.add((i,j))
            
            while q:
                i,j = q.popleft()
                
                for dx, dy in directions:
                    dx+=i
                    dy+=j

                    if dx < 0 or dx >= M or dy < 0 or dy >= N or grid[dx][dy] == "0"\
                    or (dx,dy) in visited:
                        continue
                    
                    visited.add((dx, dy))
                    q.append((dx, dy))
        
        M,N = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        
        count = 0
        
        for i in range(M):
            for j in range(N):
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs(i,j)
                    count+=1
        
        return count