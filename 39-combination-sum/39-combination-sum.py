class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def solve(idx, sm, res):
            if sm == target:
                if res not in result:
                    result.append(res[:])
                
                return
            
            if idx>=len(nums) or sm > target:
                return
            
            solve(idx, sm+nums[idx], res+[nums[idx]])
            solve(idx+1, sm, res)
        
        result = []
        
        nums.sort()
        
        solve(0, 0, [])
        
        return result