class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        
        for i, ele in enumerate(nums):
            if target-ele in mp:
                return [mp[target-ele]+1, i+1]
            
            mp[ele] = i
        