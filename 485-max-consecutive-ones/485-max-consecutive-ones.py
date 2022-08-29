class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        
        for ele in nums:
            if ele == 1:
                count+=1
                
            elif ele == 0:
                res = max(res, count)
                count = 0
        
        if count:
            res = max(res, count)
            
        return res
