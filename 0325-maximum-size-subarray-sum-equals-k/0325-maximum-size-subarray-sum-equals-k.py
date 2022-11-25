class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        result = 0
        
        mp = {}
        sm = 0
        
        for i,ele in enumerate(nums):
            sm+=ele
            
            if sm == k:
                result = max(result,i+1)
                
            if sm-k in mp:
                result = max(result,i-mp[sm-k])
                
            if sm not in mp:
                mp[sm] = i
                
        return result