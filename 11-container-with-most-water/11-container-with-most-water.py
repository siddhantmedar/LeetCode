class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        
        result = 0
        
        while left < right:
            result = max(result, (right-left)*min(nums[left], nums[right]))
            
            if nums[left] <= nums[right]:
                left+=1
                
            else:
                right-=1
                
        return result