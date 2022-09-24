class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         st = set(nums)
        
#         for i in range(n):
#             if i not in st:
#                 return i
        
#         return n
        
        n = len(nums)
        nums.sort()
    
        for i, ele in enumerate(nums):
            if i!=ele:
                return i
            
        return n
        