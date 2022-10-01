class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solve(idx, rem, res):
            if rem == 0:
                result.append(res[:])
                return
            
            if idx >= len(nums):
                return
            
            solve(idx+1, rem-1, res+[nums[idx]])
            solve(idx+1, rem, res)
            
        
        result = []
        
        nums = [i for i in range(1, n+1)]
        
        solve(0, k, [])
        
        return result