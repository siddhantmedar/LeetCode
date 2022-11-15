class Solution:
    def setZeroes(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M,N = len(nums), len(nums[0])
        row, col = False, False
        
        for j in range(N):
            if nums[0][j] == 0:
                row = True
                
        for i in range(M):
            if nums[i][0] == 0:
                col = True
                
        for i in range(1,M):
            for j in range(1,N):
                if nums[i][j] == 0:
                    nums[i][0] = 0
                    nums[0][j] = 0
                    
        for i in range(1,M):
            for j in range(1,N):
                if nums[i][0] == 0 or nums[0][j] == 0:
                    nums[i][j] = 0
        
        if row:
            for j in range(N):
                nums[0][j] = 0
        
        if col:
            for i in range(M):
                nums[i][0] = 0