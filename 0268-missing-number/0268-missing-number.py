class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        
        for ele in range(len(nums)+1):
            res^=ele
            
        for ele in nums:
            res^=ele
            
        return res