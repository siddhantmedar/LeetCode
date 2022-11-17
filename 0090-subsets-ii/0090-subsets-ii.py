class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        def solve(idx):
            nonlocal path
            
            if idx == len(nums):
                result.append(path[::])
                return
            
            path.append(nums[idx])
            solve(idx+1)
            path.pop()
            
            while idx+1<len(nums) and nums[idx] == nums[idx+1]:
                idx+=1
                
            solve(idx+1)
            
            
        result = []
        path = []
        
        solve(0)

        return result