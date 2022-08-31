class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(timer):
            nonlocal fresh
            
            changed = False
            
            for i in range(M):
                for j in range(N):
                    if grid[i][j] == timer:
                        
                        for dx, dy in directions:
                            dx+=i
                            dy+=j
                            
                            if 0<=dx<M and 0<=dy<N and grid[dx][dy] == 1:
                                grid[dx][dy] = timer+1
                                fresh-=1
                                changed = True
                   
            return changed
                        
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        M,N = len(grid), len(grid[0])
        
        count = 0
        fresh = 0
        timer = 1
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    fresh+=1
        
        while fresh:
            count+=1
            timer+=1
            
            if not bfs(timer):
                break
        
        return count if fresh == 0 else -1
        