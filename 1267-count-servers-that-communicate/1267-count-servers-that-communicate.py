class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    found = False
                    
                    for y in range(n):
                        if y != j and grid[i][y] == 1:
                            found = True
                            break
                    
                    if found: count+=1
                        
                    if not found:
                        for x in range(m):
                            if x!=i and grid[x][j] == 1:
                                found = True
                                break
                                
                        if found:
                            count+=1
                            
        return count