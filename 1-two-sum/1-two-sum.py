class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        res = None
        
        for i in range(len(nums)):
            if target-nums[i] in mp:
                res = [mp[target-nums[i]], i]
                
            mp[nums[i]] = i
            
        return res