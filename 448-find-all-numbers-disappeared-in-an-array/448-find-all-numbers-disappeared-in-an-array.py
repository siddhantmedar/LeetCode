class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        
        for i, ele in enumerate(nums):
            idx = abs(ele)-1
            
            if nums[idx] > 0:
                nums[idx]*=-1
        
        for i, ele in enumerate(nums):
            if ele > 0:
                result.append(i+1)
                
        for i, ele in enumerate(nums):
            if ele < 0:
                nums[i] = -1*ele
        
        return result
            