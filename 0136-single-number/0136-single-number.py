class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        
        for ele in nums:
            xor^=ele
            
        return xor