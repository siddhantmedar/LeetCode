class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        
        low, high = 0, len(nums)-1
        
        while low<=high:
            if nums[low] < nums[high]:
                result = min(result, nums[low])
                break
                
            mid = (low+high)>>1
            
            result = min(result, nums[mid])
            
            if nums[low] <= nums[mid]:
                low = mid+1
                
            else:
                high = mid-1
                
        return result