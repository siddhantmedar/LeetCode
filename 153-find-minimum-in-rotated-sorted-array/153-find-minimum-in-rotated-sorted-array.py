class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        
        start, end = 0, len(nums)-1
        
        while start <= end:
            mid = (start+end)>>1
            
            result = min(result, nums[mid])
            
            if nums[mid] <= nums[end]:
                end = mid-1
                
            else:
                start = mid+1
                
        return result