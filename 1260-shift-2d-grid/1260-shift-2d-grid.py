class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def getIdx(i,j):
            return i*N+j
        
        def getIndices(i):
            return i//N, i%N
        
        M,N = len(grid), len(grid[0])
        
        res = [[0 for _ in range(N)] for _ in range(M)]
        
        for i in range(M):
            for j in range(N):
                idx = getIdx(i,j)
                idx0, idx1 = getIndices((idx+k) % (M*N)) 
                
                res[idx0][idx1] = grid[i][j]
                
        return res