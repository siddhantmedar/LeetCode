class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def solve(idx):
            if idx == len(nums)-1:
                tmp.append(nums[idx])
                
                if tmp not in result:
                    result.append(tmp[:])
                
                tmp.pop()
                return
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                
                tmp.append(nums[idx])
                
                solve(idx+1)
                
                tmp.pop()
                
                nums[idx], nums[i] = nums[i], nums[idx]
                
        
        result, tmp = [], []
        
        nums.sort()
        
        solve(0)
        
        return result