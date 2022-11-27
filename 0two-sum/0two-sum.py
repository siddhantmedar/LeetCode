class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        
        for i, ele in enumerate(nums):
            if target-ele in mp:
                return [i, mp[target-ele]]
            
            mp[ele] = i
            
        return -1