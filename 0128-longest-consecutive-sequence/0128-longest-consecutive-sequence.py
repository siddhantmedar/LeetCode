class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        
        st = set(nums)
        
        for ele in nums:
            if ele-1 in st:
                continue
                
            cnt = 0
            
            while ele in st:
                cnt+=1
                ele+=1
                
            res = max(res,cnt)
            
        return res