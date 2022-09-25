class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = False, False
        M, N = len(matrix), len(matrix[0])
        
        for j in range(N):
            if matrix[0][j] == 0:
                row = True
                
        for i in range(M):
            if matrix[i][0] == 0:
                col = True
        
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, M):
            for j in range(1, N):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if row:
            for j in range(N):
                matrix[0][j] = 0
        
        if col:
            for i in range(M):
                matrix[i][0] = 0
        
        