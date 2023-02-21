class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(r,c,oldc,newc):
            if r<0 or r>=M or c<0 or c>=N or image[r][c]==newc or image[r][c] != oldc:
                return
            image[r][c] = newc
            
            for dx,dy in directions:
                dx+=r
                dy+=c
                dfs(dx,dy,oldc,newc)
        
        
        M,N = len(image), len(image[0])
        
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        
        dfs(sr,sc,image[sr][sc],color)
        
        return image
            