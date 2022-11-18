class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def solve(idx, path):
            nonlocal result
            
            if sum(path) == target:
                result.append(path[::])
                return
            
            if idx >= len(nums) or sum(path) > target:
                return
            
            solve(idx+1,path)
            solve(idx,path+[nums[idx]])
            
        
        result = []
        
        solve(0,[])
        
        return result