class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i,j,c):
            if i<0 or i>=M or j<0 or j>=N or image[i][j] != c or image[i][j] == color:
                return
            
            image[i][j] = color
            
            for dx, dy in directions:
                dx+=i
                dy+=j
                
                dfs(dx,dy,c)
            
        
        M,N = len(image),len(image[0])
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        dfs(sr,sc,image[sr][sc])
        
        return image