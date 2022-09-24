class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        
        for ele in nums:
            xor^=ele
            
        for i in range(len(nums)+1):
            xor^=i
            
        return xor