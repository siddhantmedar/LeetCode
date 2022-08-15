class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, missing = None, None
        
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            
            if nums[idx] < 0:
                dup = abs(nums[i])
                
            else:
                nums[idx] = -1*nums[idx]
                
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i+1
                break
                
        return [dup, missing]