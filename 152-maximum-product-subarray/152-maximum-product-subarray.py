class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        
        mn, mx = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            curr_mx = max(mx*nums[i], nums[i], mn*nums[i])
            curr_mn = min(mx*nums[i], nums[i], mn*nums[i])
            
            mx, mn = curr_mx, curr_mn
            
            result = max(result, mx)
        
        return result