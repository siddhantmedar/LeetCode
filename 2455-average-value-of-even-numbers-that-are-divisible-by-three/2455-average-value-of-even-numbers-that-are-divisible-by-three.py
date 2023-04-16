class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = 0
        cnt  = 0
        
        for ele in nums:
            if ele%2==0 and ele%3==0:
                res+=ele
                cnt+=1
                
        if cnt==0:
            return 0
        
        return res//cnt