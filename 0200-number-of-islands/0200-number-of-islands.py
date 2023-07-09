class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def find(x,y):
            if parent[(x,y)] != (x,y):
                parent[(x,y)] = find(parent[(x,y)][0], parent[(x,y)][1])
                
            return parent[(x,y)]
        
        def union(x,y,x_,y_):
            setX = find(x,y)
            setY = find(x_,y_)
            
            if setX != setY:
                if size[setX] >= size[setY]:
                    size[setX]+=size[setY]
                    parent[setY] = setX
                    
                else:
                    size[setY]+=size[setX]
                    parent[setX] = setY
                
        
        M,N = len(grid), len(grid[0])
        parent = {(x,y):(x,y) for x in range(M) for y in range(N) if grid[x][y] == "1"}
        size = {(x,y):1 for x in range(M) for y in range(N) if grid[x][y] == "1"}
        
        dir = [(-1,0),(1,0),(0,1),(0,-1)]
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "1":
                    for dx,dy in dir:
                        dx+=i 
                        dy+=j
                        
                        if 0<=dx<M and 0<=dy<N and grid[dx][dy] == "1":
                            union(i,j,dx,dy)
        
        return (sum([1 for k,v in parent.items() if k==v]))