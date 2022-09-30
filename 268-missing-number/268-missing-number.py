class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        
        for ele in range(0, len(nums)+1):
            result^=ele
            
        for ele in nums:
            result^=ele
            
        return result
        