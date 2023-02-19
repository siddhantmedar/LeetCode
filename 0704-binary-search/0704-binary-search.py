class Solution:
    def search(self, nums: List[int], x: int) -> int:
        low, high = 0, len(nums)-1
        
        while low<=high:
            mid = (low+high)>>1
            
            if nums[mid]==x:
                return mid
            
            if nums[mid] > x:
                high = mid-1
            
            else:
                low = mid+1
                
        return -1