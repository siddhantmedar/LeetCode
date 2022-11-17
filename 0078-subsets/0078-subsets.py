class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(idx,st):
            nonlocal result
            
            if idx >= len(nums):
                if idx == len(nums):
                    result.append(st)
                return
            
            solve(idx+1,st)
            solve(idx+1,st+[nums[idx]])
        
        result = []
        
        solve(0,[])
        
        return result