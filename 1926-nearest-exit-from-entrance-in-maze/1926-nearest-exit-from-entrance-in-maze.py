class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m,n = len(maze), len(maze[0])
        
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        res = float("inf")
        
        q = deque([(entrance[0], entrance[1], 0)])
        
        while q:
            sz = len(q)
            
            for k in range(sz):
                i,j,cost = q.popleft()
                
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    if ((i,j) != (entrance[0], entrance[1])):
                        res = min(res, cost)
                        continue
                    
                for x,y in directions:
                    x+=i
                    y+=j
                    
                    if 0<=x<m and 0<=y<n and maze[x][y] != "+":
                        maze[x][y] = "+"
                        q.append((x,y,cost+1))
                        
        return res if res != float("inf") else -1
        