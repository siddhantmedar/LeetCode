class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, high = 0, 0
        
        while high < len(nums):
            if nums[low] == 0 and nums[high] == 0:
                high+=1
            
            elif nums[low] == 0 and nums[high] != 0:
                nums[low], nums[high] = nums[high], nums[low]
                low+=1
                high+=1
                
            elif nums[low] != 0 and nums[high] == 0:
                low+=1
                high+=1
                
            elif nums[low] != 0 and nums[high] != 0:
                low+=1
                high+=1