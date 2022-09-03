class Solution:
    def trap(self, nums: List[int]) -> int:
        n = len(nums)
        
        res = 0
        
        left, right = 0, n-1
        lmxi, rmxi = nums[0], nums[n-1]

        while left < right:
            if nums[left] <= nums[right]:
                left+=1
                
                water = min(lmxi, rmxi) - nums[left]
                
                if water >= 0:
                    res+=water
                
                lmxi = max(lmxi, nums[left])
                    
            else:
                right-=1
                
                water = min(lmxi, rmxi) - nums[right]
                
                if water >= 0:
                    res+=water
                
                rmxi = max(rmxi, nums[right])

        return res