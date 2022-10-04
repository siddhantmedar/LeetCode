class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M,N = len(mat), len(mat[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        q = deque()
        result = [[float("inf") for _ in range(N)] for _ in range(M)]
        
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    
                    q.append((i,j))
                    
        
        while q:
            n = len(q)
            
            for k in range(n):
                i,j = q.popleft()
                
                for dx, dy in directions:
                    dx+=i
                    dy+=j
                    
                    if 0<=dx<M and 0<=dy<N and result[dx][dy] > 1 + result[i][j]:
                        result[dx][dy] = 1+result[i][j]
                        q.append((dx,dy))
        
        
        return result