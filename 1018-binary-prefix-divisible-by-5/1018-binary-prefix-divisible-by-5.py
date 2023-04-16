class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = [False for _ in range(len(nums))]
        pre = 0
        
        for i,ele in enumerate(nums):
            sm = pre*2+ (0 if ele == 0 else 1)
            res[i] = True if sm%5 == 0 else False
            
            pre = sm
            
        return res