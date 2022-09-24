class Solution:
    def findMin(self, nums: List[int]) -> int:
#         def isSorted(nums):
#             for i in range(len(nums)-1):
#                 if nums[i] > nums[i+1]:
#                     return False
                
#             return True
            
#         def isReverseSorted(nums):
#             for i in range(len(nums)-1):
#                 if nums[i] < nums[i+1]:
#                     return False
                
#             return True
        
#         if isSorted(nums):
#             return nums[0]
        
#         if isReverseSorted(nums):
#             return nums[len(nums)-1]
        
        start, end = 0, len(nums)-1
        
        result = nums[0]
        
        while start <= end:
            mid = (start+end)>>1
            
            result = min(result, nums[mid])
            
            if nums[mid] <= nums[end]:
                end = mid-1
                
            else:
                start = mid+1
                
        return result