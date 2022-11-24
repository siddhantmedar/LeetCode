class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i,j,pre,c):
            if i<0 or i>=M or j<0 or j>=N or image[i][j] != pre or image[i][j] == c:
                return
            
            image[i][j] = c
            
            for dx,dy in directions:
                dx+=i
                dy+=j
                
                dfs(dx,dy,pre,c)
            
        
        M,N = len(image),len(image[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        dfs(sr,sc,image[sr][sc],color)
        
        return image