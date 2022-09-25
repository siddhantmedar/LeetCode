class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(), set()
        
        M, N = len(matrix), len(matrix[0])
        
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
                    
        for i in range(M):
            for j in range(N):
                if i in row or j in col:
                    matrix[i][j] = 0
                    
        print(matrix)
        
        