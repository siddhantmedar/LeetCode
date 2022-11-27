class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        M,N = len(rooms), len(rooms[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        q = deque()
        
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j,0))
        
        while q:
            n = len(q)
            
            for _ in range(n):
                i,j,level = q.popleft()
                
                for dx,dy in directions:
                    dx+=i
                    dy+=j
                    
                    if 0<=dx<M and 0<=dy<N and (dx,dy) not in visited and rooms[dx][dy] == 2147483647:
                        rooms[dx][dy] = level+1
                        visited.add((dx,dy))
                        q.append((dx,dy,level+1))