class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M,N = len(matrix), len(matrix[0])
        
        if M == 0:
            return False
        
        start, end = 0, M*N-1
        
        while start <= end:
            mid = (start+end)>>1
            
            if matrix[mid//N][mid%N] == target:
                return True
            
            elif matrix[mid//N][mid%N] > target:
                end = mid-1
                
            else:
                start = mid+1
                
        return False
    