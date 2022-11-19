class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        i,j = 0, len(nums[0])-1
        
        while i<len(nums) and j>=0:
            if nums[i][j] == target:
                return True
            
            elif nums[i][j] > target:
                j-=1
                
            elif nums[i][j] < target:
                i+=1
                
        return False