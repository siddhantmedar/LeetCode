class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        
        curr = 0
        
        for ele in nums:
            curr = max(curr+ele, ele)
            
            result = max(result, curr)
            
        return result
        