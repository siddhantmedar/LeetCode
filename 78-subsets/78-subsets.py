class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def solve(idx, res):
            if idx == len(nums):
                result.append(res[:])
                return
            
            solve(idx+1, res+[nums[idx]])
            solve(idx+1, res)
            
        result = []
        
        solve(0,[])
        
        return result