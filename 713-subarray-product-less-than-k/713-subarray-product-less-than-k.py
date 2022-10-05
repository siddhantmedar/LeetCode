class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        i = 0
        
        prod = 1
        
        result = 0
        
        for j in range(len(nums)):
            prod*=nums[j]
            
            while prod >= k:
                prod/=nums[i]
                i+=1
                
            result+=(j-i+1)
            
        return result