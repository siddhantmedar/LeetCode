class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solve(idx):
            nonlocal path,result
            
            if idx == len(nums):
                result.append(path[::])
                return
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                path.append(nums[idx])
                solve(idx+1)
                path.pop()
                nums[idx], nums[i] = nums[i], nums[idx]
            
        
        result = []
        path = []
        
        solve(0)
        
        return result