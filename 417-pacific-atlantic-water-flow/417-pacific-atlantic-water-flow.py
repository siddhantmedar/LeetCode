class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
#         def dfs(i,j,x,y,st):
#             if i<0 or j<0 or i>=M or j>=N or (i,j) in st or grid[i][j] < grid[x][y]:
#                 return
            
#             st.add((i,j))
            
#             for dx, dy in directions:
#                 dx+=i
#                 dy+=j
                
#                 dfs(dx,dy,i,j,st)
        
        
#         M,N = len(grid), len(grid[0])
#         directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
#         pac, atl = set(), set()
        
#         for j in range(N):
#             dfs(0,j,0,j,pac)
#             dfs(M-1,j,M-1,j,atl)
            
#         for i in range(M):
#             dfs(i,0,i,0,pac)
#             dfs(i,N-1,i,N-1,atl)
        
#         return atl.intersection(pac)
    
        def bfsSolve():
            def bfs(i,j,x,y,st):
                q = deque([(i,j,x,y,st)])
                
                while q:
                    n = len(q)
                    
                    for k in range(n):
                        i,j,x,y,st = q.popleft()
            
                        if i<0 or j<0 or i>=M or j>=N or (i,j) in st or grid[i][j] < grid[x][y]:
                            continue
            
                        st.add((i,j))
            
                        for dx, dy in directions:
                            dx+=i
                            dy+=j

                            q.append((dx,dy,i,j,st))
        
        
            M,N = len(grid), len(grid[0])
            directions = [(-1,0),(1,0),(0,-1),(0,1)]

            pac, atl = set(), set()

            for j in range(N):
                bfs(0,j,0,j,pac)
                bfs(M-1,j,M-1,j,atl)

            for i in range(M):
                bfs(i,0,i,0,pac)
                bfs(i,N-1,i,N-1,atl)
                
            return atl.intersection(pac)
        

        return bfsSolve()