class Solution:
    def spiralOrder(self, nums: List[List[int]]) -> List[int]:
        M,N = len(nums), len(nums[0])
        
        result = []
        top, bottom, left, right = 0, M-1, 0, N-1
        
        dir = 1
        
        while top <= bottom and left <= right:
            if dir == 1:
                for j in range(left, right+1):
                    result.append(nums[top][j])
                    
                top+=1
                dir = 2
                
            elif dir == 2:
                for i in range(top, bottom+1):
                    result.append(nums[i][right])
                
                right-=1
                dir = 3
                
            elif dir == 3:
                for j in range(right, left-1, -1):
                    result.append(nums[bottom][j])
                    
                bottom-=1
                dir = 4
                
            elif dir == 4:
                for i in range(bottom, top-1, -1):
                    result.append(nums[i][left])
                    
                left+=1
                dir = 1
                
        return result