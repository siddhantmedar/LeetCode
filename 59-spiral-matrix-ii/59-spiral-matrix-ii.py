class Solution:
    def generateMatrix(self, N: int) -> List[List[int]]:
        matrix = [[0 for _ in range(N)] for _ in range(N)]
        
        top, bottom, left, right = 0, N-1, 0, N-1
        
        counter = 1
        
        dir = 1
        
        while top <= bottom and left <= right:
            if dir == 1:
                for j in range(left, right+1):
                    matrix[top][j] = counter
                    counter+=1
                    
                top+=1
                dir = 2
                
            elif dir == 2:
                for i in range(top, bottom+1):
                    matrix[i][right] = counter
                    counter+=1
                
                right-=1
                dir = 3
                
            elif dir == 3:
                for j in range(right, left-1, -1):
                    matrix[bottom][j] = counter
                    counter+=1
                
                bottom-=1
                dir = 4
                
            elif dir == 4:
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = counter
                    counter+=1
                    
                left+=1
                dir = 1
                
        return matrix