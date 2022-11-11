class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        
        mn, mx = nums[0], nums[0]
        
        for ele in nums[1:]:
            curr_mx = max(ele*mx, ele*mn, ele)
            curr_mn = min(ele*mx, ele*mn, ele)
            
            mx, mn = curr_mx, curr_mn
            
            result = max(result, mx)
            
        return result
        