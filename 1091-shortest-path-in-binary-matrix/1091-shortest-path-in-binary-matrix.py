class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        M,N = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
        
        q = deque()
        visited = set()
        
        if grid[0][0] == 0:
            q.append((0,0))
            visited.add((0,0))
        
        level = 0
        
        while q:
            n = len(q)
            level+=1
            
            for k in range(n):
                i,j = q.popleft()
                
                if i == M-1 and j == N-1:
                    return level
                
                for dx, dy in directions:
                    dx+=i
                    dy+=j
                    
                    if 0<=dx<M and 0<=dy<N and grid[dx][dy] == 0 and (dx,dy) not in visited:
                        visited.add((dx,dy))
                        q.append((dx,dy))
        
        return -1
        