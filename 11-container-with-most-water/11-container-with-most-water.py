class Solution:
    def maxArea(self, nums: List[int]) -> int:
        res = 0
        
        left, right = 0, len(nums)-1
        
        while left < right:
            res = max(res, min(nums[left], nums[right])*(right-left))
            
            if nums[left] <= nums[right]:
                left+=1
                
            else:
                right-=1
                
        return res
        