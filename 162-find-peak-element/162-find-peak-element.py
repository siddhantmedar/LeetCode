class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        
        while start <= end:
            if start == end:
                return start
            
            mid = (start+end) >> 1
            
            if nums[mid] > nums[mid+1]:
                end = mid
                
            else:
                start = mid+1
        