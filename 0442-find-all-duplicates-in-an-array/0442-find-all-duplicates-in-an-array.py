class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        
        for i,ele in enumerate(nums):
            idx = abs(ele)-1
            
            if nums[idx] > 0:
                nums[idx]*=-1
                
            elif nums[idx] < 0:
                result.append(abs(ele))
                
        return result