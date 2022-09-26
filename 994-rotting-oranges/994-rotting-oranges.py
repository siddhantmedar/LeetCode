class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inplace_bfs():
            def solve():
                nonlocal fresh
                
                updated = False
                
                for i in range(M):
                    for j in range(N):
                        if grid[i][j] == timestamp:
                            for dx, dy in directions:
                                dx+=i
                                dy+=j
                                
                                if 0<=dx<M and 0<=dy<N and grid[dx][dy] == 1:
                                    grid[dx][dy] = timestamp+1    
                                    fresh-=1
                                    updated = True
                                    
                                    if fresh == 0:
                                        return time
                
                return updated
            
            M,N = len(grid), len(grid[0])
            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            fresh = 0

            for i in range(M):
                for j in range(N):
                    if grid[i][j] == 1:
                        fresh+=1

            timestamp, time = 2, 0

            if fresh == 0:
                return time


            while True:
                time+=1
                result = solve()
                timestamp+=1
                
                if fresh == 0:
                    return time
                
                if not result:
                    return -1
                
        def bfs():
            M,N = len(grid), len(grid[0])
            fresh = 0
            
            q = deque()
            
            for i in range(M):
                for j in range(N):
                    if grid[i][j] == 2:
                        q.append((i,j))
                    elif grid[i][j] == 1:
                        fresh+=1
            
            time = 0
            
            if fresh == 0:
                return time
            
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            
            while q:
                n = len(q)
                time+=1
                
                for k in range(n):
                    i, j = q.popleft()
                    
                    for dx, dy in directions:
                        dx+=i
                        dy+=j
                        
                        if 0<=dx<M and 0<=dy<N and grid[dx][dy] == 1:
                            q.append((dx,dy))
                            grid[dx][dy] = 2
                            fresh-=1
                            
                            if fresh == 0:
                                return time
            
            return time if fresh == 0 else -1
        
        return inplace_bfs()
        # return bfs()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        