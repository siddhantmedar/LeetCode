class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result, sm = nums[0], nums[0]
        
        for ele in nums[1:]:
            sm = max(sm+ele, ele)
            
            result = max(result, sm)
            
        return result