class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        
        res = float("-inf")
        
        for i in range(len(nums)-1):
            res = max(res, abs(nums[i]-nums[i+1]))
            
        return res if res != float("-inf") else 0