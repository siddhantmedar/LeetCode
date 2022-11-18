class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def solve(idx,rem,path):
            nonlocal result
            
            if rem==0:
                if len(path) == k:
                    result.append(path[::]) 
                return
            
            if idx >= len(nums):
                return
            
            solve(idx+1,rem,path)
            solve(idx+1,rem-1,path+[nums[idx]])
            
            
        nums = [x for x in range(1,n+1)]
        
        result = []
        
        solve(0,k,[])
        
        return result