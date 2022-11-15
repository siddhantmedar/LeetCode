class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def process(timestamp):
            nonlocal fresh
            
            changed = False
            
            for i in range(M):
                for j in range(N):
                    if grid[i][j] == timestamp:
                        for dx, dy in directions:
                            dx+=i
                            dy+=j

                            if 0<=dx<M and 0<=dy<N and grid[dx][dy] == 1:
                                grid[dx][dy] = timestamp+1
                                changed = True
                                fresh-=1
            
            return changed
        
        
        M,N = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        fresh = 0
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    fresh+=1
        
        if fresh == 0:
            return 0
        
        time = 0
        ts = 2
        
        while True:
            time+=1
            
            if not process(ts):
                break
            
            if fresh == 0:
                return time
            
            ts+=1
        
        return -1