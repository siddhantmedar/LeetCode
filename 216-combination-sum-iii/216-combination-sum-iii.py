class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def solve(idx, sm, k, res):
            if k == 0:
                if sm == n:
                    if res not in result:
                        result.append(res[:])
                        
                return
            
            if k < 0 or sm > n or idx >= len(nums):
                return
            
            solve(idx+1, sm+nums[idx], k-1, res+[nums[idx]])
            solve(idx+1, sm, k, res)
        
        
        result = []
        
        nums = [i for i in range(1,10)]
        
        solve(0, 0, k, [])
        
        return result