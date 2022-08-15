class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i,j,x,y = 0, 0, 0, len(mat[0])-1
        
        sm = 0
        
        while (i<len(mat) and j<len(mat[0])) and (x < len(mat) and y >= 0):
            if i == x and j == y:
                sm+=mat[i][j]
                
            else:
                sm+=mat[i][j]
                sm+=mat[x][y]
                
            i+=1
            j+=1
            x+=1
            y-=1
                
        return sm