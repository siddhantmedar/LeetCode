class Solution:
    def search(self, nums: List[int], x: int) -> int:
        start, end = 0, len(nums)-1
        
        while start <= end:
            mid = (start+end)>>1
            
            if nums[mid] == x:
                return mid
            
            elif nums[start] <= nums[mid]:
                if x>=nums[start] and x<nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            
            elif nums[mid] <= nums[end]:
                if x>nums[mid] and x<=nums[end]:
                    start = mid+1
                else:
                    end = mid-1
                
        return -1