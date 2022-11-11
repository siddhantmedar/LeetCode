class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        
        return nums[0]
    
#         low, high = 0, len(nums)-1
        
#         while low < high:
#             mid = (low+high)>>1
            
#             if mid-1>0 and mid+1 < len(nums) and nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
#                 return nums[mid]
            
#             elif nums[low] <= nums[mid]:
#                 low = mid+1
                
#             else:
#                 high = mid-1
                
#         return low