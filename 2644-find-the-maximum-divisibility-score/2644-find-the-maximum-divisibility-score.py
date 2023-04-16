class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        mx = float("-inf")
        res = None
        for d in divisors:
            cnt = 0
            for ele in nums:
                cnt+=1 if ele%d==0 else 0
                
            if mx == cnt:
                res = min(res,d)
            if mx < cnt:
                mx = cnt
                res = d
            
        return res