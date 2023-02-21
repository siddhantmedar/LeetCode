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
        
        def bfs(r,c,oldc,newc):
            q = deque([(r,c)])
            
            while q:
                n = len(q)
                
                for _ in range(n):
                    r,c = q.popleft()
                        
                    image[r][c] = newc
            
                    for dx,dy in directions:
                        dx+=r
                        dy+=c
                        
                        if not (dx<0 or dx>=M or dx<0 or dy>=N or image[dx][dy]==newc or\
                        image[dx][dy] != oldc):
                            dfs(dx,dy,oldc,newc)
        
        
        M,N = len(image), len(image[0])
        
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        
        bfs(sr,sc,image[sr][sc],color)
        
        return image
            