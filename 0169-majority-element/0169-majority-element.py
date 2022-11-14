class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = {}
        
        for ele in nums:
            mp[ele] = 1+mp.get(ele,0)
            
            if mp[ele] > len(nums)//2:
                return ele