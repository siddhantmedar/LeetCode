class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mp = {}
        
        for ele in nums:
            mp[ele]  = 1+mp.get(ele, 0)
            
        for k,v in mp.items():
            if v == 1:
                return k