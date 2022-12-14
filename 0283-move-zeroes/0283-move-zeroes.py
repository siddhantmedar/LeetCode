class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         stable and non-stable positioning

        l,r = 0,0
    
        while r < len(nums):
            if nums[l]==0 and nums[r]==0:
                r+=1
                
            elif nums[l]==0 and nums[r]!=0:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r+=1
                
            else:
                l+=1
                r+=1
                
                
    
# 00->r+=1 ok
# 01->swap and l+=1,r+=1 ok
# 10->l+=1,r+=1
# 11->l+=1,r+=1