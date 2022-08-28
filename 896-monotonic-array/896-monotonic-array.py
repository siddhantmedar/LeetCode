class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def checkInc(nums):
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
                
            return True 
            
        def checkDec(nums):
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    return False
                
            return True 
        
        return checkInc(nums) or checkDec(nums)