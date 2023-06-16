class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [None]*(2*len(nums))
        
        i = 0
        
        while i < len(nums):
            res[i],res[i+len(nums)] = nums[i],nums[i]
            i+=1
            
        return res