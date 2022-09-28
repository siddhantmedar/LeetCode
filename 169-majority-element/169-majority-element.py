class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        
        for i, ele in enumerate(nums):
            mp[ele] = 1+mp.get(ele, 0)
            
        for k,v in mp.items():
            if v > len(nums) // 2:
                return k
            