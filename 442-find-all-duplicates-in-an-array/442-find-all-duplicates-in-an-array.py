class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        
        for i, ele in enumerate(nums):
            idx = abs(ele)-1
            
            if nums[idx] < 0:
                result.append(abs(ele))
                
            else:
                nums[idx]*=-1
                
        for i, ele in enumerate(nums):
            if ele < 0:
                nums[i]*=-1
                
        return result