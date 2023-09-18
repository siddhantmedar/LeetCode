class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(s,e):
            print(s,e)
            if s>e:
                return False
            
            mid=(s+e)>>1
            
            if matrix[mid//n][mid%n]==target:
                return True
            
            elif matrix[mid//n][mid%n] > target:
                return bs(s,mid-1)
            else:
                return bs(mid+1,e)
        
        
        m,n = len(matrix),len(matrix[0])
        
        return bs(0,m*n-1)
    
# for i in range(15):
#     x,y = i//5,i%5
#     print(x,y,x*5+y)