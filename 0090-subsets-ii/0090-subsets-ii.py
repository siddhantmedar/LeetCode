class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def solve(idx,path):
            nonlocal result
            
            if idx == len(nums):
                result.append(path[::])
                return
            
            solve(idx+1,path+[nums[idx]])
            
            while idx+1<len(nums) and nums[idx] == nums[idx+1]:
                idx+=1
                
            solve(idx+1,path)
            
            
        result = []
        path = []
        
        solve(0,[])

        return result