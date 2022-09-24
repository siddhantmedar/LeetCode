class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         result = []
        
#         for i in range(len(nums)):
#             product = 1
            
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
                    
#                 product*=nums[j]
                
#             result.append(product)
        
#         return result

        left, right = [1]*len(nums), [1]*len(nums)
    
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1]*nums[i+1]
        
        result = []
        
        for i in range(len(nums)):
            result.append(left[i]*right[i])
            
        return result