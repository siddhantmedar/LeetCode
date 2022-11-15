class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        top, bottom, left, right = 0, len(nums)-1, 0, len(nums[0])-1
        dir = 1
        
        while top<=bottom and left<=right:
            if dir == 1:
                for j in range(left,right+1):
                    nums[top][j] = num
                    num+=1
                
                top+=1
                dir = 2
                
            elif dir == 2:
                for i in range(top, bottom+1):
                    nums[i][right] = num
                    num+=1
                    
                right-=1
                dir = 3
            
            elif dir == 3:
                for j in range(right, left-1,-1):
                    nums[bottom][j] = num
                    num+=1
                    
                bottom-=1
                dir = 4
                
            elif dir == 4:
                for i in range(bottom, top-1,-1):
                    nums[i][left] = num
                    num+=1
                
                left+=1
                dir = 1
        
                
        return nums