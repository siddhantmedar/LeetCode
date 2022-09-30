class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        for ele in nums:
            result^=ele
            
        return result