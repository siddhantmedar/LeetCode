class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS():
            def dfs(i,j):
                if i<0 or i>=m or j<0 or j>=n or grid[i][j] == "0":
                    return

                grid[i][j] = "0"

                for x,y in directions:
                    x+=i
                    y+=j

                    dfs(x,y)
                    
            m,n = len(grid), len(grid[0])
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            count = 0
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == "1":
                        dfs(i,j)
                        count+=1
                        
            return count
        
        return DFS()
    
        def BFS():
            m,n = len(grid), len(grid[0])
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            count = 0
            
            def bfs(i,j):
                q = deque([(i,j)])

                while q:
                    sz = len(q)

                    for k in range(sz):
                        i,j = q.popleft()
                        grid[i][j] = "0"

                        for x,y in directions:
                            x+=i
                            y+=j

                            if x<0 or x>=m or y<0 or y>=n or grid[x][y] == "0":
                                continue

                            else:
                                q.append((x,y))

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == "1":
                        bfs(i,j)
                        count+=1

            return count
        
        # return BFS()
    
        def dsu():
            def find(x,y):
                if parent[(x,y)] != (x,y):
                    parent[(x,y)] = find(parent[(x,y)][0], parent[(x,y)][1])
                    
                return parent[(x,y)]
            
            def union(xa, ya, xb, yb):
                setX = find(xa,ya)
                setY = find(xb,yb)
                
                if setX != setY:
                    if size[(xa,ya)] >= size[(xb,yb)]:
                        size[(xa,ya)]+=1
                        parent[setY] = setX
                        return
                    
                    else:
                        size[(xb,yb)]+=1
                        parent[setX] = setY
                        return
                
            m,n = len(grid), len(grid[0])
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
            parent = {(i,j):(i,j) for i in range(m) for j in range(n) if grid[i][j] == "1"}
            size = {(i,j):0 for i in range(m) for j in range(n) if grid[i][j] == "1"}
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == "1":
                        for x,y in directions:
                            x+=i
                            y+=j
                            
                            if x<0 or x>=m or y<0 or y>=n or grid[x][y] == "0":
                                continue
                                
                            else:
                                union(i,j,x,y)
                                
            print(parent)
            print(grid)
            count = 0
            
            for k,v in parent.items():
                if k == v:
                    count+=1
                    
            return count
            
        # return dsu()
            
            