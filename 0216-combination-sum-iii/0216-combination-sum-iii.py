class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def solve(idx,path):
            nonlocal result
            
            if len(path) == k and sum(path) == n:
                result.append(path[::])
                return
            
            if idx >= len(nums) or len(path) > k or sum(path) > n:
                return
            
            solve(idx+1,path)
            solve(idx+1,path+[nums[idx]])
            
            
        result = []
        
        nums = [x for x in range(1,10)]
        
        solve(0,[])
        
        return result