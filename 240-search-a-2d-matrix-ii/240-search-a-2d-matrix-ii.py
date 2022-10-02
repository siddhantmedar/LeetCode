class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M,N = len(matrix), len(matrix[0])
        
        row = 0
        col = N-1
        
        while 0<=row<M and 0<=col<N:
            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] > target:
                col-=1
                
            else:
                row+=1
                
        return False