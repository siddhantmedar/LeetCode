class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        
        while start <= end:
            mid = (start+end)>>1
            
            if mid-1 >= 0 and mid+1 < len(nums) and nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            elif mid-1 >= 0 and nums[mid-1] > nums[mid]:
                end = mid-1
                
            else:
                start = mid+1
        