class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        M,N = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        q = deque()
        visited = set()
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "*":
                    q.append((i,j))
                    visited.add((i,j))
                    break
        
        level = 0
        
        while q:
            n = len(q)
            
            for k in range(n):
                i,j = q.popleft()
                
                if grid[i][j] == "#":
                    return level
                
                for dx, dy in directions:
                    dx+=i
                    dy+=j
                    
                    if 0<=dx<M and 0<=dy<N and (grid[dx][dy] == "O" or grid[dx][dy] == "#")\
                                                and (dx,dy) not in visited:
                        visited.add((dx,dy))
                        q.append((dx,dy))
            
            level+=1
        
        
        return -1




# ["#","O","O"]
# ["O","*","O"]



















        
# ["X","X","X","X","X","X"]
# ["X","*","O","O","O","X"]
# ["X","O","O","#","O","X"]
# ["X","X","X","X","X","X"]

# ["X","X","X","X","X"]
# ["X","*","X","O","X"]
# ["X","O","X","#","X"]
# ["X","X","X","X","X"]

# ["X","X","X","X","X","X","X","X"]
# ["X","*","O","X","O","#","O","X"]
# ["X","O","O","X","O","O","X","X"]
# ["X","O","O","O","O","#","O","X"]
# ["X","X","X","X","X","X","X","X"]