class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res = [0 for _ in range(len(grid[0]))]
        
        for j in range(len(grid[0])):
            mx = 0
            for i in range(len(grid)):
                mx = max(mx, len(str(grid[i][j])))
                
            res[j] = mx
            
        return res