class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = deque()
        
        l,r = 0, len(nums)-1
        
        while l<=r:
            if nums[l]**2 <= nums[r]**2:
                result.appendleft(nums[r]**2)
                r-=1
                
            else:
                result.appendleft(nums[l]**2)
                l+=1
        
        return result
        