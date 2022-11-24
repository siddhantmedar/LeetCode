class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        m,n = len(matrix),len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                idx = abs(matrix[i][j])-1
                
                if matrix[i][idx] < 0:
                    return False
                
                matrix[i][idx]*=-1
                
        for i in range(m):
            for j in range(n):
                idx = abs(matrix[j][i])-1
                
                if matrix[idx][i] > 0:
                    return False
                
                matrix[idx][i]*=-1
        
        return True