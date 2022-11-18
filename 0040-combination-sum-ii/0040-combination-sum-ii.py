class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        def solve(idx,path):
            nonlocal result
            
            if sum(path) == target:
                result.append(path[::])
                return
            
            if idx >= len(nums) or sum(path) > target:
                return
            
            solve(idx+1,path+[nums[idx]])
            
            while idx+1<len(nums) and nums[idx] == nums[idx+1]:
                idx+=1
                
            solve(idx+1,path)
            
            
        result = []
        path = []
        
        solve(0,[])

        return result