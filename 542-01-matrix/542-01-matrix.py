class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M,N = len(mat), len(mat[0])
        directions = [(-1,0), (1,0), (0,-1),(0,1)]
        
        dist = [[0 for _ in range(N)] for _ in range(M)]
        
        q = deque()
        
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i,j))
                elif mat[i][j] == 1:
                    dist[i][j] = float("inf")
        
        while q:
            n = len(q)
            
            for i in range(len(q)):
                i,j = q.popleft()
                
                for x,y in directions:
                    x+=i
                    y+=j
                    if 0<=x<M and 0<=y<N and dist[x][y] > dist[i][j]+1:
                        dist[x][y] = dist[i][j]+1
                        q.append((x,y))
                        
        return dist