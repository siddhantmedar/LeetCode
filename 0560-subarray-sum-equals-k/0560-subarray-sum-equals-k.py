class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        
        mp = {0:1}
        sm = 0
        
        for ele in nums:
            sm+=ele
            result+=mp.get(sm-k,0)
            
            mp[sm] = 1+mp.get(sm,0)
            
        return result