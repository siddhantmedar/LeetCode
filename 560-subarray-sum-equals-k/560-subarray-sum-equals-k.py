class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        
        mp = {0:1}
        
        prefix = 0
        
        for i, ele in enumerate(nums):
            prefix+=ele
            
            if prefix-k in mp:
                result+=mp[prefix-k]
                
            mp[prefix] = 1+mp.get(prefix,0)
            
        return result