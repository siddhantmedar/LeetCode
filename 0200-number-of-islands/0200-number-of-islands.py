class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def find(x,y):
            if parent[(x,y)] != (x,y):
                parent[(x,y)] = find(parent[(x,y)][0], parent[(x,y)][1])
                
            return parent[(x,y)]
        
        def union(i,j,x,y):
            setX = find(i,j)
            setY = find(x,y)
            
            if setX != setY:
                if size[setX] >= size[setY]:
                    size[setX]+=1
                    parent[setY] = setX
                    
                else:
                    size[setY]+=1
                    parent[setX] = setY
            
            
        M,N = len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        parent = {(i,j):(i,j) for i in range(M) for j in range(N) if grid[i][j] == "1"}
        size = {(i,j):1 for i in range(M) for j in range(N) if grid[i][j] == "1"}
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    for dx,dy in directions:
                        dx+=i
                        dy+=j
                        
                        if 0<=dx<M and 0<=dy<N and grid[dx][dy] == "1":
                            union(i,j,dx,dy)
        
        return sum([1 for k,v in parent.items() if k == v])