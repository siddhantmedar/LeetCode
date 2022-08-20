class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = float("-inf")
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        res = max(res, nums[j]-nums[i])
                        
        return res if res!= float("-inf") else -1