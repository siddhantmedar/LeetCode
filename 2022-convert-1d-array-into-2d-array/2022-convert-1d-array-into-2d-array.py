class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        
        result = [[0 for _ in range(n)] for _ in range(m)]
        
        for i,ele in enumerate(original):
            result[i//n][i%n] = ele
            
        return result