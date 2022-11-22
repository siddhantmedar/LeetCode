class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        row, col = defaultdict(set), defaultdict(set)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                row[i].add(matrix[i][j])
                col[j].add(matrix[i][j])
        
        for k,v in row.items():
            if len(v) != len(matrix):
                return False
            
        for k,v in col.items():
            if len(v) != len(matrix):
                return False
        
        return True