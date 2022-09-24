class Solution:
    def maxArea(self, nums: List[int]) -> int:
#         result = 0
        
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 result = max(result, (j-i)*min(nums[i], nums[j]))
                
#         return result

        result = 0
        left, right = 0, len(nums)-1
    
        while left < right:
            result = max(result, (right-left)*min(nums[left], nums[right]))
            
            if nums[left] <= nums[right]:
                left+=1
                
            else:
                right-=1
                
        return result
                
                