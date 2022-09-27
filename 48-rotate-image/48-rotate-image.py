class Solution:
    def rotate(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l, r = 0, len(grid)-1
        
        while l < r:
            for i in range(r-l):
                t, b = l, r
            
                tmp = grid[t][l+i]
                
                grid[t][l+i] = grid[b-i][l]
                grid[b-i][l] = grid[b][r-i]
                grid[b][r-i] = grid[t+i][r]
                grid[t+i][r] = tmp
                
            l+=1
            r-=1
        
        