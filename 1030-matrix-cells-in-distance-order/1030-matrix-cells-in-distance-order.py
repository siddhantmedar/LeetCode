class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res = [[i,j] for i in range(rows) for j in range(cols)]
        
        return sorted(res,key=lambda x: abs(x[0]-rCenter)+abs(x[1]-cCenter))