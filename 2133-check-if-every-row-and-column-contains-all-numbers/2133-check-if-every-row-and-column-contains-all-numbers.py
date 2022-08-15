class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        st = set([i for i in range(1, len(matrix)+1)])
        
        for i in range(len(matrix)):
            if st != set(matrix[i]) or\
            st != set([matrix[j][i] for j in range(len(matrix[0]))]):
                return False
        
        return True
    
    
    
        
