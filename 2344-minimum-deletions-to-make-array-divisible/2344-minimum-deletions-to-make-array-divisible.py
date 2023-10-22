class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        mp = Counter(sorted(nums))
        print(mp)
        cnt = 0
        
        for k,v in mp.items():
            if all(x%k==0 for x in numsDivide):
                return cnt
            
            cnt+=v
            
        return cnt if cnt < len(nums) else -1