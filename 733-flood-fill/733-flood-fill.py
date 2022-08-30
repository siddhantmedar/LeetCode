class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i,j, new_color, old_color):
            if i<0 or i>=M or j<0 or j>=N or image[i][j] != old_color or image[i][j] == new_color:
                return
            
            image[i][j] = new_color
            
            dfs(i-1,j, new_color, old_color)
            dfs(i+1,j, new_color, old_color)
            dfs(i,j-1, new_color, old_color)
            dfs(i,j+1, new_color, old_color)
        
        M,N = len(image), len(image[0])
        
        dfs(sr,sc, color, image[sr][sc])
        
        return image
        